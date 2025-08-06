# Collatz Data Science Project 🔢

[![CI/CD Pipeline](https://github.com/username/collatz-data-science/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/username/collatz-data-science/actions/workflows/ci-cd.yml)
[![Security Scan](https://github.com/username/collatz-data-science/actions/workflows/security.yml/badge.svg)](https://github.com/username/collatz-data-science/actions/workflows/security.yml)
[![Performance Tests](https://github.com/username/collatz-data-science/actions/workflows/performance.yml/badge.svg)](https://github.com/username/collatz-data-science/actions/workflows/performance.yml)
[![Documentation](https://github.com/username/collatz-data-science/actions/workflows/docs.yml/badge.svg)](https://github.com/username/collatz-data-science/actions/workflows/docs.yml)
[![codecov](https://codecov.io/gh/username/collatz-data-science/branch/main/graph/badge.svg)](https://codecov.io/gh/username/collatz-data-science)

A comprehensive data science project for analyzing and exploring the Collatz conjecture (3n+1 problem) using modern tools and methodologies.

## 🎯 Project Overview

The Collatz conjecture is one of mathematics' most famous unsolved problems. This project provides:

- **Scalable computation** of Collatz sequences
- **PostgreSQL database** with optimized schema for sequence storage
- **Interactive analysis** tools and Jupyter notebooks
- **Web dashboard** for visualization and exploration
- **Comprehensive testing** and performance monitoring
- **Production-ready CI/CD** pipeline

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker & Docker Compose
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/collatz-data-science.git
   cd collatz-data-science
   ```

2. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start the database:**
   ```bash
   docker-compose up -d database
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run tests:**
   ```bash
   pytest
   ```

## 🏗️ Architecture

### Database Schema

The PostgreSQL database includes:

- **6 tables** for storing sequences, analysis results, and metadata
- **10 views** for efficient querying and analysis
- **6 custom functions** for sequence calculations
- **33 indexes** for optimal performance

### Key Components

```
collatz-data-science/
├── src/                    # Python source code
├── tests/                  # Test suite
├── notebooks/              # Jupyter notebooks
├── sql/                    # Database schema and migrations
├── dashboard/              # Web dashboard application
├── .github/workflows/      # CI/CD pipelines
└── docker-compose.yml      # Container orchestration
```

## 🔄 CI/CD Pipeline

Our comprehensive CI/CD pipeline includes:

### Main Pipeline (`ci-cd.yml`)
- **Testing & Linting**: pytest, flake8, black, isort, mypy
- **Security Scanning**: safety, bandit
- **Docker Build**: Multi-platform container images
- **Notebook Testing**: Automated notebook execution
- **Deployment**: Staging and production environments

### Security Pipeline (`security.yml`)
- **Vulnerability Scanning**: Safety, Bandit, Semgrep
- **Container Security**: Trivy scanning
- **Code Analysis**: CodeQL analysis
- **Secret Detection**: TruffleHog, GitLeaks

### Performance Pipeline (`performance.yml`)
- **Benchmark Testing**: Performance regression detection
- **Memory Profiling**: Memory usage analysis
- **Database Performance**: Query optimization testing

### Documentation Pipeline (`docs.yml`)
- **Sphinx Documentation**: Auto-generated API docs
- **Notebook Processing**: Jupyter notebook documentation
- **GitHub Pages**: Automated documentation deployment

## 🧪 Testing Strategy

### Test Categories

- **Unit Tests**: Core algorithm testing
- **Integration Tests**: Database and API testing
- **Performance Tests**: Benchmark and regression testing
- **Security Tests**: Vulnerability and compliance testing

### Running Tests

```bash
# All tests
pytest

# Specific categories
pytest -m "unit"              # Unit tests only
pytest -m "integration"       # Integration tests only
pytest -m "not slow"          # Skip slow tests
pytest -m "database"          # Database tests only

# With coverage
pytest --cov=src --cov-report=html
```

## 📊 Database Connection

### pgAdmin Setup

To connect to the database using pgAdmin:

**Connection Settings:**
- **Host:** `localhost`
- **Port:** `5432`
- **Database:** `collatz_db`
- **Username:** `postgresql`
- **Password:** `weaknaweak27`

### Database Features

- **Optimized Schema**: Efficient storage and querying
- **Custom Functions**: PostgreSQL functions for calculations
- **Performance Views**: Pre-computed statistics and analysis
- **Indexing Strategy**: Comprehensive indexing for fast queries

## 🛠️ Development

### Code Quality

We maintain high code quality using:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting and style checking
- **mypy**: Static type checking
- **pre-commit**: Automated quality checks

### Pre-commit Setup

```bash
pip install pre-commit
pre-commit install
```

### Development Workflow

1. Create feature branch
2. Make changes
3. Run tests locally
4. Commit (pre-commit hooks run automatically)
5. Push and create PR
6. CI/CD pipeline runs automatically
7. Review and merge

## 🚀 Deployment

### Environments

- **Development**: Local development environment
- **Staging**: Automated deployment from `develop` branch
- **Production**: Automated deployment from releases

### Container Registry

Docker images are automatically built and pushed to GitHub Container Registry:

```bash
docker pull ghcr.io/username/collatz-data-science:latest
```

## 📈 Performance

### Benchmarks

- **Small numbers (< 1000)**: < 1ms per calculation
- **Medium numbers (< 10000)**: < 10ms per calculation
- **Large numbers (< 100000)**: < 100ms per calculation
- **Database queries**: < 50ms for most operations

### Monitoring

- Automated performance regression detection
- Memory usage profiling
- Database performance metrics
- CI/CD pipeline performance tracking

## 🔒 Security

### Security Measures

- **Dependency Scanning**: Automated vulnerability detection
- **Code Analysis**: Static security analysis
- **Container Scanning**: Docker image vulnerability scanning
- **Secret Detection**: Automated secret scanning
- **Dependabot**: Automated dependency updates

### Security Policies

- No secrets in code or configuration files
- Regular security updates via Dependabot
- Comprehensive security scanning in CI/CD
- Security-focused code review process

## 📚 Documentation

- **API Documentation**: Auto-generated from code
- **User Guide**: Comprehensive usage instructions
- **Developer Guide**: Development and contribution guidelines
- **Database Schema**: Complete database documentation
- **Jupyter Notebooks**: Interactive tutorials and examples

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed
- Ensure all CI/CD checks pass
- Write clear commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The mathematical community studying the Collatz conjecture
- Open source contributors and maintainers
- The Python data science ecosystem

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/username/collatz-data-science/issues)
- **Discussions**: [GitHub Discussions](https://github.com/username/collatz-data-science/discussions)
- **Documentation**: [Project Documentation](https://username.github.io/collatz-data-science/)

---

**Made with ❤️ for mathematics and data science**