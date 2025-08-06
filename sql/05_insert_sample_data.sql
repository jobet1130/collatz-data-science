-- Sample Data for Collatz Data Science Database
-- This file inserts sample data for development and testing

-- Insert sample Collatz sequences for numbers 1-20
INSERT INTO collatz_sequences (starting_number, sequence_length, max_value, total_steps, stopping_time) VALUES
(1, 0, 1, 0, 0),
(2, 1, 2, 1, 1),
(3, 7, 16, 7, 7),
(4, 2, 4, 2, 2),
(5, 5, 16, 5, 5),
(6, 8, 16, 8, 8),
(7, 16, 52, 16, 16),
(8, 3, 8, 3, 3),
(9, 19, 52, 19, 19),
(10, 6, 16, 6, 6),
(11, 14, 52, 14, 14),
(12, 9, 16, 9, 9),
(13, 9, 40, 9, 9),
(14, 17, 52, 17, 17),
(15, 17, 160, 17, 17),
(16, 4, 16, 4, 4),
(17, 12, 52, 12, 12),
(18, 20, 52, 20, 20),
(19, 20, 88, 20, 20),
(20, 7, 20, 7, 7)
ON CONFLICT (starting_number) DO NOTHING;

-- Insert some sample analysis results
INSERT INTO analysis_results (
    analysis_type, 
    range_start, 
    range_end, 
    total_sequences, 
    avg_sequence_length, 
    max_sequence_length, 
    min_sequence_length, 
    avg_max_value, 
    analysis_duration_seconds,
    metadata
) VALUES
(
    'basic_range_analysis',
    1,
    20,
    20,
    10.15,
    20,
    0,
    42.8,
    0.125,
    '{"algorithm": "iterative", "optimization": "none"}'
),
(
    'sequence_distribution',
    1,
    100,
    100,
    12.45,
    118,
    0,
    156.7,
    2.340,
    '{"algorithm": "parallel", "threads": 4, "chunk_size": 25}'
),
(
    'peak_value_analysis',
    1,
    1000,
    1000,
    15.23,
    178,
    0,
    2847.3,
    45.678,
    '{"algorithm": "optimized", "cache_enabled": true, "memory_limit": "1GB"}'
);

-- Insert sample experiments
INSERT INTO experiments (
    experiment_name,
    description,
    parameters,
    status,
    start_time,
    end_time,
    results,
    created_by
) VALUES
(
    'Initial Range Test',
    'Testing Collatz sequences for numbers 1-1000',
    '{"range_start": 1, "range_end": 1000, "batch_size": 100, "parallel": true}',
    'completed',
    CURRENT_TIMESTAMP - INTERVAL '2 hours',
    CURRENT_TIMESTAMP - INTERVAL '1 hour 45 minutes',
    '{"total_processed": 1000, "avg_length": 15.23, "max_length": 178, "errors": 0}',
    'system'
),
(
    'Large Number Analysis',
    'Analyzing sequences for large starting numbers',
    '{"range_start": 10000, "range_end": 20000, "batch_size": 500, "timeout": 300}',
    'running',
    CURRENT_TIMESTAMP - INTERVAL '30 minutes',
    NULL,
    NULL,
    'researcher'
),
(
    'Performance Benchmark',
    'Benchmarking different algorithms for sequence calculation',
    '{"algorithms": ["iterative", "recursive", "memoized"], "test_range": 10000}',
    'pending',
    NULL,
    NULL,
    NULL,
    'developer'
);

-- Insert sample batch jobs
INSERT INTO batch_jobs (
    job_name,
    job_type,
    range_start,
    range_end,
    batch_size,
    status,
    progress_percentage,
    processed_count,
    total_count,
    start_time
) VALUES
(
    'Daily Processing Job',
    'sequence_calculation',
    1,
    10000,
    1000,
    'completed',
    100.00,
    10000,
    10000,
    CURRENT_TIMESTAMP - INTERVAL '6 hours'
),
(
    'Weekly Analysis',
    'statistical_analysis',
    1,
    50000,
    5000,
    'running',
    65.40,
    32700,
    50000,
    CURRENT_TIMESTAMP - INTERVAL '2 hours'
),
(
    'Data Validation',
    'validation',
    1,
    1000,
    100,
    'queued',
    0.00,
    0,
    1000,
    NULL
);

-- Insert sample performance metrics
INSERT INTO performance_metrics (metric_name, metric_value, metric_unit, context) VALUES
('sequence_calculation_time', 0.0023, 'seconds', '{"algorithm": "iterative", "number": 27}'),
('sequence_calculation_time', 0.0045, 'seconds', '{"algorithm": "iterative", "number": 127}'),
('sequence_calculation_time', 0.0156, 'seconds', '{"algorithm": "iterative", "number": 871}'),
('memory_usage', 45.6, 'MB', '{"operation": "batch_processing", "batch_size": 1000}'),
('memory_usage', 123.4, 'MB', '{"operation": "batch_processing", "batch_size": 5000}'),
('cpu_utilization', 78.5, 'percent', '{"operation": "parallel_processing", "threads": 4}'),
('cpu_utilization', 92.1, 'percent', '{"operation": "parallel_processing", "threads": 8}'),
('database_query_time', 0.012, 'seconds', '{"query_type": "range_select", "range_size": 1000}'),
('database_query_time', 0.045, 'seconds', '{"query_type": "range_select", "range_size": 10000}'),
('throughput', 2340.5, 'sequences_per_second', '{"algorithm": "optimized", "parallel": true}');

-- Insert some sequence steps for detailed analysis (only for smaller sequences)
INSERT INTO sequence_steps (sequence_id, step_number, value, operation)
SELECT 
    cs.id,
    1,
    CASE WHEN cs.starting_number % 2 = 0 THEN cs.starting_number / 2 ELSE cs.starting_number * 3 + 1 END,
    CASE WHEN cs.starting_number % 2 = 0 THEN 'divide' ELSE 'multiply' END
FROM collatz_sequences cs
WHERE cs.starting_number <= 10 AND cs.starting_number > 1;

-- Add more detailed steps for sequence starting with 3
INSERT INTO sequence_steps (sequence_id, step_number, value, operation)
SELECT cs.id, 2, 5, 'multiply' FROM collatz_sequences cs WHERE cs.starting_number = 3
UNION ALL
SELECT cs.id, 3, 16, 'multiply' FROM collatz_sequences cs WHERE cs.starting_number = 3
UNION ALL
SELECT cs.id, 4, 8, 'divide' FROM collatz_sequences cs WHERE cs.starting_number = 3
UNION ALL
SELECT cs.id, 5, 4, 'divide' FROM collatz_sequences cs WHERE cs.starting_number = 3
UNION ALL
SELECT cs.id, 6, 2, 'divide' FROM collatz_sequences cs WHERE cs.starting_number = 3
UNION ALL
SELECT cs.id, 7, 1, 'divide' FROM collatz_sequences cs WHERE cs.starting_number = 3;

COMMIT;

-- Display sample data summary
SELECT 'Sample data inserted successfully!' as status;
SELECT 'Collatz sequences: ' || COUNT(*) as sequences_count FROM collatz_sequences;
SELECT 'Analysis results: ' || COUNT(*) as analysis_count FROM analysis_results;
SELECT 'Experiments: ' || COUNT(*) as experiments_count FROM experiments;
SELECT 'Batch jobs: ' || COUNT(*) as jobs_count FROM batch_jobs;
SELECT 'Performance metrics: ' || COUNT(*) as metrics_count FROM performance_metrics;
SELECT 'Sequence steps: ' || COUNT(*) as steps_count FROM sequence_steps;