-- Views for Collatz Data Science Database
-- This file creates useful views for common queries and analytics

-- View for sequence statistics summary
CREATE OR REPLACE VIEW sequence_statistics AS
SELECT 
    COUNT(*) as total_sequences,
    MIN(starting_number) as min_starting_number,
    MAX(starting_number) as max_starting_number,
    AVG(sequence_length)::DECIMAL(10,2) as avg_sequence_length,
    MIN(sequence_length) as min_sequence_length,
    MAX(sequence_length) as max_sequence_length,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY sequence_length) as median_sequence_length,
    AVG(max_value)::DECIMAL(15,2) as avg_max_value,
    MIN(max_value) as min_max_value,
    MAX(max_value) as max_max_value,
    AVG(total_steps)::DECIMAL(10,2) as avg_total_steps,
    MIN(total_steps) as min_total_steps,
    MAX(total_steps) as max_total_steps,
    COUNT(CASE WHEN stopping_time IS NOT NULL THEN 1 END) as sequences_with_stopping_time
FROM collatz_sequences;

-- View for sequence length distribution
CREATE OR REPLACE VIEW sequence_length_distribution AS
SELECT 
    sequence_length,
    COUNT(*) as frequency,
    COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () as percentage
FROM collatz_sequences
GROUP BY sequence_length
ORDER BY sequence_length;

-- View for top longest sequences
CREATE OR REPLACE VIEW top_longest_sequences AS
SELECT 
    starting_number,
    sequence_length,
    max_value,
    total_steps,
    stopping_time,
    created_at
FROM collatz_sequences
ORDER BY sequence_length DESC, max_value DESC
LIMIT 100;

-- View for sequences with highest peak values
CREATE OR REPLACE VIEW top_peak_sequences AS
SELECT 
    starting_number,
    sequence_length,
    max_value,
    total_steps,
    stopping_time,
    created_at
FROM collatz_sequences
ORDER BY max_value DESC, sequence_length DESC
LIMIT 100;

-- View for recent analysis summary
CREATE OR REPLACE VIEW recent_analysis_summary AS
SELECT 
    analysis_type,
    range_start,
    range_end,
    total_sequences,
    avg_sequence_length,
    max_sequence_length,
    min_sequence_length,
    avg_max_value,
    analysis_duration_seconds,
    created_at
FROM analysis_results
ORDER BY created_at DESC
LIMIT 50;

-- View for experiment status overview
CREATE OR REPLACE VIEW experiment_status_overview AS
SELECT 
    status,
    COUNT(*) as count,
    COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () as percentage
FROM experiments
GROUP BY status
ORDER BY count DESC;

-- View for active experiments
CREATE OR REPLACE VIEW active_experiments AS
SELECT 
    id,
    experiment_name,
    description,
    status,
    start_time,
    CASE 
        WHEN start_time IS NOT NULL AND end_time IS NULL 
        THEN EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - start_time))/60
        ELSE NULL 
    END as running_minutes,
    created_by,
    created_at
FROM experiments
WHERE status IN ('pending', 'running')
ORDER BY start_time DESC NULLS LAST;

-- View for batch job progress
CREATE OR REPLACE VIEW batch_job_progress AS
SELECT 
    id,
    job_name,
    job_type,
    range_start,
    range_end,
    status,
    progress_percentage,
    processed_count,
    total_count,
    CASE 
        WHEN total_count > 0 
        THEN (processed_count * 100.0 / total_count)::DECIMAL(5,2)
        ELSE 0 
    END as calculated_progress,
    CASE 
        WHEN start_time IS NOT NULL AND end_time IS NULL 
        THEN EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - start_time))/60
        WHEN start_time IS NOT NULL AND end_time IS NOT NULL
        THEN EXTRACT(EPOCH FROM (end_time - start_time))/60
        ELSE NULL 
    END as duration_minutes,
    created_at,
    updated_at
FROM batch_jobs
ORDER BY created_at DESC;

-- View for performance metrics summary
CREATE OR REPLACE VIEW performance_summary AS
SELECT 
    metric_name,
    COUNT(*) as measurement_count,
    AVG(metric_value)::DECIMAL(15,6) as avg_value,
    MIN(metric_value) as min_value,
    MAX(metric_value) as max_value,
    STDDEV(metric_value)::DECIMAL(15,6) as std_deviation,
    metric_unit,
    MIN(recorded_at) as first_recorded,
    MAX(recorded_at) as last_recorded
FROM performance_metrics
GROUP BY metric_name, metric_unit
ORDER BY metric_name;

-- View for daily sequence processing stats
CREATE OR REPLACE VIEW daily_processing_stats AS
SELECT 
    DATE(created_at) as processing_date,
    COUNT(*) as sequences_processed,
    AVG(sequence_length)::DECIMAL(10,2) as avg_length,
    MAX(sequence_length) as max_length,
    AVG(max_value)::DECIMAL(15,2) as avg_peak_value,
    MAX(max_value) as max_peak_value
FROM collatz_sequences
GROUP BY DATE(created_at)
ORDER BY processing_date DESC;

COMMIT;