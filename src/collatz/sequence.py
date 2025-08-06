"""Collatz sequence generation and analysis functions"""

def collatz_sequence(n):
    """
    Generate the complete Collatz sequence for a given starting number.
    
    Args:
        n (int): Starting number (must be positive)
        
    Returns:
        list: Complete Collatz sequence from n to 1
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Starting number must be a positive integer")
    
    sequence = []
    current = n
    
    while current != 1:
        sequence.append(current)
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    
    sequence.append(1)  # Add the final 1
    return sequence

def collatz_length(n):
    """
    Calculate the length of the Collatz sequence for a given starting number.
    
    Args:
        n (int): Starting number (must be positive)
        
    Returns:
        int: Length of the Collatz sequence
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Starting number must be a positive integer")
    
    length = 0
    current = n
    
    while current != 1:
        length += 1
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    
    length += 1  # Count the final 1
    return length

def collatz_max_value(n):
    """
    Find the maximum value reached in the Collatz sequence for a given starting number.
    
    Args:
        n (int): Starting number (must be positive)
        
    Returns:
        int: Maximum value reached in the sequence
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Starting number must be a positive integer")
    
    max_value = n
    current = n
    
    while current != 1:
        if current > max_value:
            max_value = current
        
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    
    return max_value

def collatz_steps_to_max(n):
    """
    Find the number of steps to reach the maximum value in the Collatz sequence.
    
    Args:
        n (int): Starting number (must be positive)
        
    Returns:
        int: Number of steps to reach the maximum value
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Starting number must be a positive integer")
    
    max_value = n
    max_steps = 0
    current = n
    steps = 0
    
    while current != 1:
        if current > max_value:
            max_value = current
            max_steps = steps
        
        steps += 1
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    
    return max_steps

def is_power_of_two(n):
    """
    Check if a number is a power of 2.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is a power of 2, False otherwise
    """
    return n > 0 and (n & (n - 1)) == 0

def collatz_analysis(n):
    """
    Perform complete analysis of a Collatz sequence.
    
    Args:
        n (int): Starting number (must be positive)
        
    Returns:
        dict: Dictionary containing sequence analysis results
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Starting number must be a positive integer")
    
    sequence = collatz_sequence(n)
    
    return {
        'starting_number': n,
        'sequence_length': len(sequence),
        'max_value': max(sequence),
        'steps_to_max': sequence.index(max(sequence)),
        'sequence': sequence,
        'is_power_of_two': is_power_of_two(n),
        'even_steps': sum(1 for x in sequence if x % 2 == 0),
        'odd_steps': sum(1 for x in sequence if x % 2 == 1)
    }