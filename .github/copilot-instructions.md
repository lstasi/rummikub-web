# Rummikub Web Application

Rummikub Web is a frontend web application for playing the classic tile-laying game Rummikub online. The repository is currently in early development stage with minimal setup.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the information here.

## Repository Status

**IMPORTANT**: This repository is currently minimal with only a README.md file. It represents a fresh project setup that has not yet been implemented. When working with this codebase, expect to potentially create the initial project structure.

## Working Effectively

### Current Repository State
- The repository currently contains only:
  - `README.md` - Basic project description
  - `.git/` - Git repository metadata
  - No build files, dependencies, or source code yet

### Expected Development Setup (When Implemented)
Based on the project name and typical web frontend patterns, this will likely become a modern web application. When the project is implemented, expect the following structure:

- **Frontend Framework**: Likely React, Vue, or Angular
- **Package Management**: npm or yarn
- **Build Tools**: Webpack, Vite, or similar
- **Testing**: Jest, Cypress, or similar
- **Styling**: CSS modules, styled-components, or CSS frameworks

### Bootstrap Commands (When Project Files Exist)
When the project has been implemented with standard web tooling:

1. Install dependencies:
   ```bash
   npm install
   ```
   - Expected time: 1-3 minutes
   - NEVER CANCEL: May take longer on slower networks

2. Build the application:
   ```bash
   npm run build
   ```
   - Expected time: 30 seconds to 5 minutes depending on project size
   - NEVER CANCEL: Set timeout to 10+ minutes for safety

3. Run development server:
   ```bash
   npm run dev
   # or
   npm start
   ```
   - Expected time: 10-30 seconds to start
   - Server typically runs on http://localhost:3000 or similar

4. Run tests:
   ```bash
   npm test
   ```
   - Expected time: 10 seconds to 5 minutes depending on test suite size
   - NEVER CANCEL: Set timeout to 15+ minutes for comprehensive test suites

### Linting and Code Quality (When Implemented)
Always run these before committing changes:
```bash
npm run lint          # Check code style and errors
npm run format        # Auto-format code (if configured)
npm run type-check    # TypeScript type checking (if using TypeScript)
```

## Validation

### Manual Testing Scenarios
When the application is implemented, ALWAYS test these scenarios after making changes:

1. **Game Setup Flow**:
   - Start a new game
   - Set up players
   - Initialize the tile rack
   - Verify tiles display correctly

2. **Game Play Flow**:
   - Place tiles on the board
   - Form valid runs and groups
   - Draw tiles from the pool
   - Pass turn to next player
   - Complete a full game round

3. **UI Responsiveness**:
   - Test on different screen sizes
   - Verify mobile/tablet layouts
   - Check touch interactions work properly

### Browser Testing
- Test in Chrome, Firefox, Safari, and Edge
- Verify WebSocket connections work (if multiplayer is implemented)
- Test with browser developer tools console open to check for errors

### Performance Validation
- Check for memory leaks during long gaming sessions
- Verify smooth animations and interactions
- Test with multiple concurrent games (if supported)

## Common Tasks

### Creating New Features
1. Always start by understanding the game rules and requirements
2. Create components in a modular, reusable way
3. Follow established patterns for state management
4. Add appropriate tests for new functionality
5. Update documentation as needed

### Debugging Issues
1. Use browser developer tools extensively
2. Check console for JavaScript errors
3. Inspect network requests for API calls
4. Use React DevTools (or equivalent) for component debugging
5. Test game logic with various tile combinations

### Adding Dependencies
Always document the purpose of new dependencies:
```bash
npm install [package-name]
# Document in comments why this dependency was added
```

## Project Structure (Expected When Implemented)

```
/
├── README.md                 # Current project documentation
├── package.json             # Dependencies and scripts (when created)
├── src/                     # Source code directory (when created)
│   ├── components/          # Reusable UI components
│   ├── pages/              # Application pages/views
│   ├── hooks/              # Custom React hooks (if React)
│   ├── utils/              # Utility functions
│   ├── types/              # TypeScript definitions
│   └── assets/             # Static assets (images, sounds)
├── public/                  # Public static files
├── tests/                   # Test files
└── docs/                    # Additional documentation
```

## Important Notes

- **Game Rules**: Familiarize yourself with official Rummikub rules before implementing features
- **Accessibility**: Ensure the game is playable with keyboard navigation and screen readers
- **Multiplayer**: If implementing multiplayer, consider real-time synchronization challenges
- **Mobile First**: Design with mobile/tablet gameplay in mind
- **Performance**: Tile animations and drag-drop should be smooth and responsive

## CI/CD Expectations

When CI/CD is set up (likely in `.github/workflows/`), expect:
- Automated testing on pull requests
- Build verification
- Code quality checks
- Deployment to staging/production environments

## Development Workflow

1. Always work on feature branches
2. Write tests for new functionality
3. Ensure code passes all linting and formatting checks
4. Test manually in browser before creating pull requests
5. Document any game rule implementations or UI decisions

## Troubleshooting

### Common Issues (When Project Exists)
- **Node version**: Ensure using correct Node.js version (check `.nvmrc` if it exists)
- **Port conflicts**: Development server port may be in use
- **Memory issues**: Large game states may cause performance problems
- **WebSocket failures**: Check network configuration for multiplayer features

### Getting Help
- Check the official Rummikub rules for game logic questions
- Review existing code patterns before implementing new features
- Use browser developer tools for debugging UI issues
- Test across different devices and browsers regularly

---

**Remember**: This repository is currently minimal. When implementing features, follow modern web development best practices and maintain consistency with established patterns in the codebase.