# Contributing to Constitutional AI

Thank you for your interest in contributing to Constitutional AI! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please be respectful and professional in all interactions.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Environment details (OS, browser, versions)

### Suggesting Features

We welcome feature suggestions! Please:
- Check if the feature is already requested
- Provide clear use case and rationale
- Describe expected behavior
- Consider legal research workflow impact

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow code style guidelines
   - Write tests for new features
   - Update documentation

4. **Test your changes**
   ```bash
   # Frontend
   cd frontend && npm test
   
   # Backend
   cd backend && pytest
   ```

5. **Commit with clear messages**
   ```bash
   git commit -m "feat: add citation verification feature"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Describe what changes you made
   - Reference any related issues
   - Ensure all tests pass

## Development Guidelines

### Frontend (React/TypeScript)

#### Code Style
- Use TypeScript for all new code
- Follow ESLint rules
- Use Prettier for formatting
- Prefer functional components with hooks

#### Component Structure
```typescript
import React from 'react';

interface Props {
  // Define props
}

export const ComponentName: React.FC<Props> = ({ prop1, prop2 }) => {
  // Component logic
  
  return (
    <div className="component-name">
      {/* JSX */}
    </div>
  );
};
```

#### Naming Conventions
- Components: PascalCase (e.g., `QueryInterface.tsx`)
- Files: PascalCase for components, camelCase for utilities
- CSS classes: kebab-case (e.g., `query-input`)
- Functions: camelCase (e.g., `handleSubmit`)

### Backend (Python/FastAPI)

#### Code Style
- Follow PEP 8 guidelines
- Use type hints for all functions
- Write docstrings for public functions
- Use Black for formatting

#### Function Structure
```python
def process_legal_query(
    query: str,
    jurisdiction: Optional[str] = None
) -> LegalQueryResponse:
    """
    Process a legal query and return grounded answer.
    
    Args:
        query: The legal question to process
        jurisdiction: Optional jurisdiction filter
        
    Returns:
        LegalQueryResponse with answer and citations
        
    Raises:
        ValueError: If query is invalid
    """
    # Implementation
```

#### Naming Conventions
- Files: snake_case (e.g., `query_service.py`)
- Classes: PascalCase (e.g., `LegalRetriever`)
- Functions: snake_case (e.g., `verify_citation`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_QUERY_LENGTH`)

### Testing

#### Frontend Tests
```typescript
describe('QueryInterface', () => {
  it('should validate query input', () => {
    // Test implementation
  });
});
```

#### Backend Tests
```python
def test_verify_citation():
    """Test citation verification logic"""
    # Test implementation
    assert result.valid is True
```

### Commit Messages

Follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add devil's advocate mode
fix: correct citation verification logic
docs: update API documentation
```

## Legal-Specific Guidelines

### Citation Handling
- Always verify citations before display
- Include source metadata
- Check for amendments
- Validate jurisdiction applicability

### Content Accuracy
- Never fabricate legal sources
- Always cite original documents
- Mark uncertain information clearly
- Include confidence scores

### Privacy & Security
- No user data in logs
- Sanitize all inputs
- Secure API keys
- Follow data protection laws

## Project-Specific Notes

### RAG Pipeline Changes
When modifying the RAG pipeline:
1. Test with diverse legal queries
2. Verify citation accuracy
3. Check hallucination rates
4. Measure performance impact
5. Update documentation

### Database Schema Changes
1. Create migration scripts
2. Test with sample data
3. Update models and schemas
4. Document changes

### API Changes
1. Update OpenAPI schema
2. Version endpoints if breaking
3. Update client code
4. Document in API.md

## Review Process

1. **Automated checks** - CI/CD pipeline runs tests
2. **Code review** - Maintainer reviews code
3. **Legal validation** - For legal logic changes
4. **Testing** - Manual testing if needed
5. **Merge** - Approved PRs are merged

## Getting Help

- GitHub Discussions: Ask questions
- GitHub Issues: Report bugs or request features
- Email: dev@constitutional-ai.com

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project website (when launched)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Constitutional AI! Your efforts help make legal research more accessible and reliable.
