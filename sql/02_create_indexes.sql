-- Indexes for Collatz Data Science Database
-- This file creates indexes to optimize query performance

-- Indexes for collatz_sequences table
CREATE INDEX IF NOT EXISTS idx_collatz_sequences_starting_number ON collatz_sequences(starting_number);
CREATE INDEX IF NOT EXISTS idx_collatz_sequences_sequence_length ON collatz_sequences(sequence_length);
CREATE INDEX IF NOT EXISTS idx_collatz_sequences_max_value ON collatz_sequences(max_value);
CREATE INDEX IF NOT EXISTS idx_collatz_sequences_total_steps ON collatz_sequences(total_steps);
CREATE INDEX IF NOT EXISTS idx_collatz_sequences_stopping_time ON collatz_sequences(stopping_time);
CREATE INDEX IF NOT EXISTS idx_collatz_sequences_created_at ON collatz_sequences(created_at);

-- Composite index for range queries
CREATE INDEX IF NOT EXISTS idx_collatz_sequences_range_length ON collatz_sequences(starting_number, sequence_length);

-- Indexes for sequence_steps table
CREATE INDEX IF NOT EXISTS idx_sequence_steps_sequence_id ON sequence_steps(sequence_id);
CREATE INDEX IF NOT EXISTS idx_sequence_steps_step_number ON sequence_steps(step_number);
CREATE INDEX IF NOT EXISTS idx_sequence_steps_value ON sequence_steps(value);
CREATE INDEX IF NOT EXISTS idx_sequence_steps_operation ON sequence_steps(operation);

-- Indexes for analysis_results table
CREATE INDEX IF NOT EXISTS idx_analysis_results_type ON analysis_results(analysis_type);
CREATE INDEX IF NOT EXISTS idx_analysis_results_range ON analysis_results(range_start, range_end);
CREATE INDEX IF NOT EXISTS idx_analysis_results_created_at ON analysis_results(created_at);
CREATE INDEX IF NOT EXISTS idx_analysis_results_avg_length ON analysis_results(avg_sequence_length);

-- Indexes for experiments table
CREATE INDEX IF NOT EXISTS idx_experiments_name ON experiments(experiment_name);
CREATE INDEX IF NOT EXISTS idx_experiments_status ON experiments(status);
CREATE INDEX IF NOT EXISTS idx_experiments_created_by ON experiments(created_by);
CREATE INDEX IF NOT EXISTS idx_experiments_created_at ON experiments(created_at);
CREATE INDEX IF NOT EXISTS idx_experiments_start_time ON experiments(start_time);

-- Indexes for batch_jobs table
CREATE INDEX IF NOT EXISTS idx_batch_jobs_name ON batch_jobs(job_name);
CREATE INDEX IF NOT EXISTS idx_batch_jobs_type ON batch_jobs(job_type);
CREATE INDEX IF NOT EXISTS idx_batch_jobs_status ON batch_jobs(status);
CREATE INDEX IF NOT EXISTS idx_batch_jobs_range ON batch_jobs(range_start, range_end);
CREATE INDEX IF NOT EXISTS idx_batch_jobs_created_at ON batch_jobs(created_at);
CREATE INDEX IF NOT EXISTS idx_batch_jobs_progress ON batch_jobs(progress_percentage);

-- Indexes for performance_metrics table
CREATE INDEX IF NOT EXISTS idx_performance_metrics_name ON performance_metrics(metric_name);
CREATE INDEX IF NOT EXISTS idx_performance_metrics_recorded_at ON performance_metrics(recorded_at);
CREATE INDEX IF NOT EXISTS idx_performance_metrics_name_time ON performance_metrics(metric_name, recorded_at);

-- GIN index for JSONB columns to enable efficient JSON queries
CREATE INDEX IF NOT EXISTS idx_analysis_results_metadata_gin ON analysis_results USING GIN(metadata);
CREATE INDEX IF NOT EXISTS idx_experiments_parameters_gin ON experiments USING GIN(parameters);
CREATE INDEX IF NOT EXISTS idx_experiments_results_gin ON experiments USING GIN(results);
CREATE INDEX IF NOT EXISTS idx_performance_metrics_context_gin ON performance_metrics USING GIN(context);

COMMIT;