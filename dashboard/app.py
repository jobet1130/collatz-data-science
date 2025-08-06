"""Main application entry point for the Collatz Data Science project.

This module provides a simple web interface and health check endpoint.
"""

import os
import logging
from typing import Dict, Any

try:
    from flask import Flask, jsonify, request
except ImportError:
    # Fallback if Flask is not available
    Flask = None
    jsonify = None
    request = None

from src.collatz.core import analyze_sequence, batch_analyze, find_longest_sequence

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_app() -> 'Flask':
    """Create and configure the Flask application.
    
    Returns:
        Configured Flask application instance.
    """
    if Flask is None:
        raise ImportError("Flask is required but not installed")
        
    app = Flask(__name__)
    
    # Configure app
    app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() == 'true'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    @app.route('/health')
    def health_check() -> Dict[str, Any]:
        """Health check endpoint.
        
        Returns:
            JSON response indicating service health.
        """
        return jsonify({
            'status': 'healthy',
            'service': 'collatz-data-science',
            'version': '0.1.0',
            'environment': os.getenv('ENVIRONMENT', 'development')
        })
    
    @app.route('/')
    def index() -> Dict[str, Any]:
        """Root endpoint with basic information.
        
        Returns:
            JSON response with service information.
        """
        return jsonify({
            'message': 'Welcome to Collatz Data Science API',
            'version': '0.1.0',
            'endpoints': {
                'health': '/health',
                'analyze': '/analyze/<int:number>',
                'batch': '/batch/<int:start>/<int:end>',
                'longest': '/longest/<int:start>/<int:end>'
            }
        })
    
    @app.route('/analyze/<int:number>')
    def analyze_endpoint(number: int) -> Dict[str, Any]:
        """Analyze a single Collatz sequence.
        
        Args:
            number: The starting number for the sequence.
            
        Returns:
            JSON response with sequence analysis.
        """
        try:
            if number <= 0:
                return jsonify({'error': 'Number must be positive'}), 400
                
            analysis = analyze_sequence(number)
            return jsonify(analysis)
            
        except Exception as e:
            logger.error(f"Error analyzing sequence for {number}: {e}")
            return jsonify({'error': str(e)}), 500
    
    @app.route('/batch/<int:start>/<int:end>')
    def batch_endpoint(start: int, end: int) -> Dict[str, Any]:
        """Analyze multiple Collatz sequences in a range.
        
        Args:
            start: Starting number (inclusive).
            end: Ending number (inclusive).
            
        Returns:
            JSON response with batch analysis results.
        """
        try:
            if start <= 0 or end <= 0:
                return jsonify({'error': 'Numbers must be positive'}), 400
                
            if end - start > 1000:
                return jsonify({'error': 'Range too large (max 1000)'}), 400
                
            results = batch_analyze(start, end)
            return jsonify({
                'start': start,
                'end': end,
                'count': len(results),
                'results': results
            })
            
        except Exception as e:
            logger.error(f"Error in batch analysis {start}-{end}: {e}")
            return jsonify({'error': str(e)}), 500
    
    @app.route('/longest/<int:start>/<int:end>')
    def longest_endpoint(start: int, end: int) -> Dict[str, Any]:
        """Find the longest Collatz sequence in a range.
        
        Args:
            start: Starting number (inclusive).
            end: Ending number (inclusive).
            
        Returns:
            JSON response with the longest sequence analysis.
        """
        try:
            if start <= 0 or end <= 0:
                return jsonify({'error': 'Numbers must be positive'}), 400
                
            if end - start > 10000:
                return jsonify({'error': 'Range too large (max 10000)'}), 400
                
            longest = find_longest_sequence(start, end)
            return jsonify({
                'range': f'{start}-{end}',
                'longest_sequence': longest
            })
            
        except Exception as e:
            logger.error(f"Error finding longest sequence {start}-{end}: {e}")
            return jsonify({'error': str(e)}), 500
    
    return app


def main():
    """Main entry point for the application."""
    try:
        app = create_app()
        port = int(os.getenv('PORT', 8080))
        host = os.getenv('HOST', '0.0.0.0')
        
        logger.info(f"Starting Collatz Data Science API on {host}:{port}")
        app.run(host=host, port=port, debug=app.config['DEBUG'])
        
    except ImportError as e:
        logger.error(f"Missing dependencies: {e}")
        logger.info("Running in basic mode without web interface")
        
        # Basic functionality test
        logger.info("Testing core functionality...")
        result = analyze_sequence(27)
        logger.info(f"Collatz(27) analysis: {result}")
        
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise


if __name__ == '__main__':
    main()