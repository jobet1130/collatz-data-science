-- Collatz Data Science Database Schema
-- This file creates the main tables for storing Collatz sequence data and analysis results

-- Table to store individual Collatz sequences
CREATE TABLE IF NOT EXISTS collatz_sequences (
    id SERIAL PRIMARY KEY,
    starting_number BIGINT NOT NULL,
    sequence_length INTEGER NOT NULL,
    max_value BIGINT NOT NULL,
    total_steps INTEGER NOT NULL,
    stopping_time INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(starting_number)
);

-- Table to store detailed sequence steps (optional, for smaller sequences)
CREATE TABLE IF NOT EXISTS sequence_steps (
    id SERIAL PRIMARY KEY,
    sequence_id INTEGER REFERENCES collatz_sequences(id) ON DELETE CASCADE,
    step_number INTEGER NOT NULL,
    value BIGINT NOT NULL,
    operation VARCHAR(10) NOT NULL CHECK (operation IN ('divide', 'multiply')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(sequence_id, step_number)
);

-- Table to store analysis results and statistics
CREATE TABLE IF NOT EXISTS analysis_results (
    id SERIAL PRIMARY KEY,
    analysis_type VARCHAR(50) NOT NULL,
    range_start BIGINT NOT NULL,
    range_end BIGINT NOT NULL,
    total_sequences INTEGER NOT NULL,
    avg_sequence_length DECIMAL(10,2),
    max_sequence_length INTEGER,
    min_sequence_length INTEGER,
    avg_max_value DECIMAL(15,2),
    analysis_duration_seconds DECIMAL(10,3),
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store experiment configurations and results
CREATE TABLE IF NOT EXISTS experiments (
    id SERIAL PRIMARY KEY,
    experiment_name VARCHAR(100) NOT NULL,
    description TEXT,
    parameters JSONB NOT NULL,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'running', 'completed', 'failed')),
    start_time TIMESTAMP WITH TIME ZONE,
    end_time TIMESTAMP WITH TIME ZONE,
    results JSONB,
    error_message TEXT,
    created_by VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store batch processing jobs
CREATE TABLE IF NOT EXISTS batch_jobs (
    id SERIAL PRIMARY KEY,
    job_name VARCHAR(100) NOT NULL,
    job_type VARCHAR(50) NOT NULL,
    range_start BIGINT NOT NULL,
    range_end BIGINT NOT NULL,
    batch_size INTEGER DEFAULT 1000,
    status VARCHAR(20) DEFAULT 'queued' CHECK (status IN ('queued', 'running', 'completed', 'failed', 'cancelled')),
    progress_percentage DECIMAL(5,2) DEFAULT 0.00,
    processed_count INTEGER DEFAULT 0,
    total_count INTEGER,
    start_time TIMESTAMP WITH TIME ZONE,
    end_time TIMESTAMP WITH TIME ZONE,
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store performance metrics
CREATE TABLE IF NOT EXISTS performance_metrics (
    id SERIAL PRIMARY KEY,
    metric_name VARCHAR(50) NOT NULL,
    metric_value DECIMAL(15,6) NOT NULL,
    metric_unit VARCHAR(20),
    context JSONB,
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

COMMIT;