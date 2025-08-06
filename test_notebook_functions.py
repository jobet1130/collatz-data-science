#!/usr/bin/env python3
"""
Test script to verify that the notebook functions work correctly
and generate some sample visualizations.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collatz.sequence import collatz_sequence, collatz_length

def test_collatz_functions():
    """Test basic Collatz functions"""
    print("Testing Collatz functions...")
    
    # Test some known values
    test_cases = [
        (1, 1),
        (2, 2), 
        (3, 8),
        (4, 3),
        (5, 6)
    ]
    
    for num, expected_length in test_cases:
        actual_length = collatz_length(num)
        sequence = collatz_sequence(num)
        print(f"Number {num}: Length {actual_length} (expected {expected_length}), Sequence: {sequence}")
        assert actual_length == expected_length, f"Length mismatch for {num}"
    
    print("✓ All basic tests passed!")

def generate_sample_data():
    """Generate sample data for visualization"""
    print("\nGenerating sample data for numbers 1-100...")
    
    numbers = range(1, 101)
    sequence_data = []
    
    for num in numbers:
        if num % 20 == 0:
            print(f"Progress: {num}/100")
        
        length = collatz_length(num)
        sequence = collatz_sequence(num)
        max_value = max(sequence) if sequence else num
        
        sequence_data.append({
            'starting_number': num,
            'sequence_length': length,
            'max_value': max_value
        })
    
    return pd.DataFrame(sequence_data)

def create_visualizations(df):
    """Create sample visualizations"""
    print("\nCreating visualizations...")
    
    # Set up the plot style
    plt.style.use('default')  # Use default instead of seaborn
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Scatter plot of sequence lengths
    axes[0, 0].scatter(df['starting_number'], df['sequence_length'], alpha=0.7, c='blue')
    axes[0, 0].set_title('Sequence Length vs Starting Number')
    axes[0, 0].set_xlabel('Starting Number')
    axes[0, 0].set_ylabel('Sequence Length')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Histogram of sequence lengths
    axes[0, 1].hist(df['sequence_length'], bins=15, alpha=0.7, color='green', edgecolor='black')
    axes[0, 1].set_title('Distribution of Sequence Lengths')
    axes[0, 1].set_xlabel('Sequence Length')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Max values (log scale)
    axes[1, 0].scatter(df['starting_number'], df['max_value'], alpha=0.7, c='red')
    axes[1, 0].set_title('Maximum Value vs Starting Number')
    axes[1, 0].set_xlabel('Starting Number')
    axes[1, 0].set_ylabel('Maximum Value')
    axes[1, 0].set_yscale('log')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Top 10 longest sequences
    top_10 = df.nlargest(10, 'sequence_length')
    axes[1, 1].bar(range(len(top_10)), top_10['sequence_length'], color='orange', alpha=0.7)
    axes[1, 1].set_title('Top 10 Longest Sequences')
    axes[1, 1].set_xlabel('Rank')
    axes[1, 1].set_ylabel('Sequence Length')
    axes[1, 1].set_xticks(range(len(top_10)))
    axes[1, 1].set_xticklabels([f'{num}' for num in top_10['starting_number']], rotation=45)
    
    plt.tight_layout()
    plt.savefig('collatz_analysis_sample.png', dpi=150, bbox_inches='tight')
    print("✓ Visualizations saved as 'collatz_analysis_sample.png'")
    plt.show()

def print_statistics(df):
    """Print summary statistics"""
    print("\n" + "="*50)
    print("COLLATZ SEQUENCE ANALYSIS SUMMARY")
    print("="*50)
    print(f"Numbers analyzed: {len(df)}")
    print(f"Average sequence length: {df['sequence_length'].mean():.2f}")
    print(f"Median sequence length: {df['sequence_length'].median():.2f}")
    print(f"Standard deviation: {df['sequence_length'].std():.2f}")
    print(f"Shortest sequence: {df['sequence_length'].min()} (number: {df.loc[df['sequence_length'].idxmin(), 'starting_number']})")
    print(f"Longest sequence: {df['sequence_length'].max()} (number: {df.loc[df['sequence_length'].idxmax(), 'starting_number']})")
    print(f"Range: {df['sequence_length'].max() - df['sequence_length'].min()}")
    
    print("\nTop 10 longest sequences:")
    top_10 = df.nlargest(10, 'sequence_length')[['starting_number', 'sequence_length', 'max_value']]
    print(top_10.to_string(index=False))

if __name__ == "__main__":
    try:
        # Test the functions
        test_collatz_functions()
        
        # Generate data
        df = generate_sample_data()
        
        # Create visualizations
        create_visualizations(df)
        
        # Print statistics
        print_statistics(df)
        
        print("\n✓ All tests completed successfully!")
        print("The notebook should now work properly with comprehensive visualizations.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()