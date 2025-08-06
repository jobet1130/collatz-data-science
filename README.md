# Collatz Data Science Project

[![CI/CD Pipeline](https://github.com/jobet1130/collatz-data-science/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/jobet1130/collatz-data-science/actions/workflows/ci-cd.yml)
[![Security Scan](https://github.com/jobet1130/collatz-data-science/actions/workflows/security.yml/badge.svg)](https://github.com/jobet1130/collatz-data-science/actions/workflows/security.yml)
[![Performance Tests](https://github.com/jobet1130/collatz-data-science/actions/workflows/performance.yml/badge.svg)](https://github.com/jobet1130/collatz-data-science/actions/workflows/performance.yml)
[![Documentation](https://github.com/jobet1130/collatz-data-science/actions/workflows/docs.yml/badge.svg)](https://github.com/jobet1130/collatz-data-science/actions/workflows/docs.yml)

A comprehensive data science project for analyzing and visualizing Collatz sequences (also known as the 3n+1 problem). This project provides tools for sequence generation, statistical analysis, performance benchmarking, and interactive visualization.

## 🔢 About the Collatz Conjecture

The Collatz conjecture is one of the most famous unsolved problems in mathematics. For any positive integer n:
- If n is even, divide it by 2
- If n is odd, multiply by 3 and add 1
- Repeat until reaching 1

The conjecture states that this sequence will always eventually reach 1, regardless of the starting number.

## ✨ Features

### Core Functionality
- **Sequence Generation**: Generate complete Collatz sequences for any positive integer
- **Statistical Analysis**: Calculate sequence length, maximum value, and convergence patterns
- **Performance Optimization**: Numba-accelerated computations for large-scale analysis
- **Database Integration**: PostgreSQL storage for sequence data and analysis results

### Visualization & Analysis
- **Interactive Dashboards**: Streamlit-based web interface for exploration
- **Jupyter Notebooks**: Comprehensive analysis and visualization examples
- **Statistical Plots**: Sequence length distributions, convergence patterns, and more
- **Performance Benchmarks**: Detailed timing and memory usage analysis

### Development & Deployment
- **Containerized**: Docker support for consistent environments
- **CI/CD Pipeline**: Automated testing, security scanning, and deployment
- **Code Quality**: Black, isort, flake8, and mypy integration
- **Comprehensive Testing**: Unit tests, integration tests, and performance benchmarks

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Pull the latest image
docker pull jobet95/collatz-data-science:latest

# Run the dashboard
docker run -p 8080:8080 jobet95/collatz-data-science:latest

# Access the dashboard at http://localhost:8080
```

### Local Installation

```bash
# Clone the repository
git clone https://github.com/jobet1130/collatz-data-science.git
cd collatz-data-science

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## 📖 Usage

### Basic Sequence Analysis

```python
from src.collatz.sequence import collatz_sequence, collatz_analysis

# Generate a Collatz sequence
sequence = collatz_sequence(27)
print(f"Sequence for 27: {sequence}")
# Output: [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]

# Get comprehensive analysis
analysis = collatz_analysis(27)
print(f"Analysis: {analysis}")
# Output: {'sequence_length': 111, 'max_value': 9232, 'steps_to_max': 77, 'is_power_of_two': False}
```

### Running the Dashboard

```bash
# Start the Streamlit dashboard
streamlit run dashboard/app.py

# Or using the module
python -m dashboard
```

### Jupyter Notebooks

```bash
# Start Jupyter Lab
jupyter lab

# Open the analysis notebook
# Navigate to notebooks/01_collatz_analysis.ipynb
```

## 🗄️ Database Setup

The project supports PostgreSQL for storing sequence data and analysis results.

### Using Docker Compose

```bash
# Start PostgreSQL and the application
docker-compose up -d

# The database will be available at localhost:5432
# Default credentials: postgresql/password
```

### Manual Setup

```bash
# Create database
createdb collatz_db

# Run SQL scripts
psql -d collatz_db -f sql/01_create_tables.sql
psql -d collatz_db -f sql/02_create_indexes.sql
psql -d collatz_db -f sql/03_create_views.sql
psql -d collatz_db -f sql/04_create_functions.sql
psql -d collatz_db -f sql/05_insert_sample_data.sql
```

### Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit database connection settings
# DATABASE_URL=postgresql://username:password@localhost:5432/collatz_db
```

## 🧪 Testing

### Run All Tests

```bash
# Run the complete test suite
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test categories
pytest -m unit          # Unit tests only
pytest -m integration   # Integration tests only
pytest -m slow          # Performance tests
```

### Performance Benchmarks

```bash
# Run benchmark tests
pytest --benchmark-only

# Generate benchmark report
pytest --benchmark-only --benchmark-html=reports/benchmark.html
```

## 🔧 Development

### Code Quality

```bash
# Format code
black src/ tests/
isort src/ tests/

# Lint code
flake8 src/ tests/
mypy src/

# Security scan
bandit -r src/
safety check
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

### Building Docker Images

```bash
# Build locally
docker build -t collatz-data-science .

# Build with specific tag
docker build -t collatz-data-science:v1.0.0 .

# Run locally built image
docker run -p 8080:8080 collatz-data-science
```

## 📊 Project Structure

```
collatz-data-science/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD
├── dashboard/              # Streamlit dashboard
├── data/
│   ├── processed/          # Processed datasets
│   └── raw/               # Raw data files
├── notebooks/             # Jupyter analysis notebooks
├── reports/               # Generated reports and outputs
├── sql/                   # Database schema and queries
├── src/
│   └── collatz/           # Core sequence analysis module
├── tests/                 # Test suite
├── docker-compose.yml     # Multi-container setup
├── Dockerfile            # Container definition
├── requirements.txt      # Python dependencies
└── pyproject.toml        # Project configuration
```

## 🚢 Deployment

### Docker Hub

Images are automatically built and pushed to Docker Hub on releases:

```bash
# Pull latest release
docker pull jobet95/collatz-data-science:latest

# Pull specific version
docker pull jobet95/collatz-data-science:v1.0.0
```

### GitHub Container Registry

Alternatively, pull from GitHub Container Registry:

```bash
docker pull ghcr.io/jobet95/collatz-data-science:latest
```

### Production Deployment

For production deployment, see [DOCKER_HUB_SETUP.md](DOCKER_HUB_SETUP.md) for detailed configuration instructions.

### Troubleshooting

**GitHub Container Registry Permission Issues**: If you encounter "installation not allowed to Create organization package" errors, see [GITHUB_CONTAINER_REGISTRY_SETUP.md](GITHUB_CONTAINER_REGISTRY_SETUP.md) for solutions.

## 📈 Performance

The project includes comprehensive performance optimization:

- **Numba JIT compilation** for computational hot paths
- **Vectorized operations** using NumPy
- **Database indexing** for efficient queries
- **Memory profiling** and optimization
- **Benchmark tracking** across versions

### Benchmark Results

| Operation | Input Size | Time (ms) | Memory (MB) |
|-----------|------------|-----------|-------------|
| Sequence Generation | n=1000 | 0.15 | 0.1 |
| Batch Analysis | 1000 numbers | 45.2 | 2.3 |
| Database Insert | 1000 records | 123.5 | 1.8 |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive tests for new features
- Update documentation for API changes
- Use type hints for all functions
- Add docstrings for public methods

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Collatz Conjecture (Wikipedia)](https://en.wikipedia.org/wiki/Collatz_conjecture)
- [OEIS Sequence A006577](https://oeis.org/A006577) - Number of steps to reach 1
- [Project Documentation](https://jobet1130.github.io/collatz-data-science/)
- [Docker Hub Repository](https://hub.docker.com/r/jobet95/collatz-data-science)

## 🙏 Acknowledgments

- Lothar Collatz for the fascinating mathematical conjecture
- The Python scientific computing community
- Contributors and maintainers of the dependencies used

---