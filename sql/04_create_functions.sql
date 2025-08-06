-- Functions and Triggers for Collatz Data Science Database
-- This file creates utility functions and triggers for automation

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Function to calculate Collatz sequence length
CREATE OR REPLACE FUNCTION calculate_collatz_length(n BIGINT)
RETURNS INTEGER AS $$
DECLARE
    current_val BIGINT := n;
    steps INTEGER := 0;
BEGIN
    IF n <= 0 THEN
        RETURN NULL;
    END IF;
    
    WHILE current_val != 1 LOOP
        IF current_val % 2 = 0 THEN
            current_val := current_val / 2;
        ELSE
            current_val := current_val * 3 + 1;
        END IF;
        steps := steps + 1;
        
        -- Safety check to prevent infinite loops
        IF steps > 10000 THEN
            RETURN NULL;
        END IF;
    END LOOP;
    
    RETURN steps;
END;
$$ LANGUAGE plpgsql;

-- Function to calculate Collatz sequence maximum value
CREATE OR REPLACE FUNCTION calculate_collatz_max(n BIGINT)
RETURNS BIGINT AS $$
DECLARE
    current_val BIGINT := n;
    max_val BIGINT := n;
    steps INTEGER := 0;
BEGIN
    IF n <= 0 THEN
        RETURN NULL;
    END IF;
    
    WHILE current_val != 1 LOOP
        IF current_val % 2 = 0 THEN
            current_val := current_val / 2;
        ELSE
            current_val := current_val * 3 + 1;
        END IF;
        
        IF current_val > max_val THEN
            max_val := current_val;
        END IF;
        
        steps := steps + 1;
        
        -- Safety check to prevent infinite loops
        IF steps > 10000 THEN
            RETURN max_val;
        END IF;
    END LOOP;
    
    RETURN max_val;
END;
$$ LANGUAGE plpgsql;

-- Function to get sequence statistics for a range
CREATE OR REPLACE FUNCTION get_range_statistics(start_num BIGINT, end_num BIGINT)
RETURNS TABLE(
    range_start BIGINT,
    range_end BIGINT,
    total_sequences BIGINT,
    avg_length DECIMAL(10,2),
    max_length INTEGER,
    min_length INTEGER,
    avg_max_value DECIMAL(15,2),
    max_max_value BIGINT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        start_num as range_start,
        end_num as range_end,
        COUNT(*)::BIGINT as total_sequences,
        AVG(cs.sequence_length)::DECIMAL(10,2) as avg_length,
        MAX(cs.sequence_length) as max_length,
        MIN(cs.sequence_length) as min_length,
        AVG(cs.max_value)::DECIMAL(15,2) as avg_max_value,
        MAX(cs.max_value) as max_max_value
    FROM collatz_sequences cs
    WHERE cs.starting_number BETWEEN start_num AND end_num;
END;
$$ LANGUAGE plpgsql;

-- Function to insert or update sequence data
CREATE OR REPLACE FUNCTION upsert_collatz_sequence(
    p_starting_number BIGINT,
    p_sequence_length INTEGER DEFAULT NULL,
    p_max_value BIGINT DEFAULT NULL,
    p_total_steps INTEGER DEFAULT NULL,
    p_stopping_time INTEGER DEFAULT NULL
)
RETURNS INTEGER AS $$
DECLARE
    sequence_id INTEGER;
    calculated_length INTEGER;
    calculated_max BIGINT;
BEGIN
    -- Calculate missing values if not provided
    IF p_sequence_length IS NULL THEN
        calculated_length := calculate_collatz_length(p_starting_number);
    ELSE
        calculated_length := p_sequence_length;
    END IF;
    
    IF p_max_value IS NULL THEN
        calculated_max := calculate_collatz_max(p_starting_number);
    ELSE
        calculated_max := p_max_value;
    END IF;
    
    -- Insert or update the sequence
    INSERT INTO collatz_sequences (
        starting_number, 
        sequence_length, 
        max_value, 
        total_steps, 
        stopping_time
    )
    VALUES (
        p_starting_number,
        calculated_length,
        calculated_max,
        COALESCE(p_total_steps, calculated_length),
        p_stopping_time
    )
    ON CONFLICT (starting_number) 
    DO UPDATE SET
        sequence_length = EXCLUDED.sequence_length,
        max_value = EXCLUDED.max_value,
        total_steps = EXCLUDED.total_steps,
        stopping_time = EXCLUDED.stopping_time,
        updated_at = CURRENT_TIMESTAMP
    RETURNING id INTO sequence_id;
    
    RETURN sequence_id;
END;
$$ LANGUAGE plpgsql;

-- Function to clean up old performance metrics
CREATE OR REPLACE FUNCTION cleanup_old_metrics(days_to_keep INTEGER DEFAULT 30)
RETURNS INTEGER AS $$
DECLARE
    deleted_count INTEGER;
BEGIN
    DELETE FROM performance_metrics 
    WHERE recorded_at < CURRENT_TIMESTAMP - INTERVAL '1 day' * days_to_keep;
    
    GET DIAGNOSTICS deleted_count = ROW_COUNT;
    RETURN deleted_count;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_collatz_sequences_updated_at
    BEFORE UPDATE ON collatz_sequences
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_experiments_updated_at
    BEFORE UPDATE ON experiments
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_batch_jobs_updated_at
    BEFORE UPDATE ON batch_jobs
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

COMMIT;