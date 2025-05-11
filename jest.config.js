module.exports = {
  projects: [
    {
      displayName: 'web',
      testMatch: ['<rootDir>/apps/web/src/**/*.test.(ts|tsx|js|jsx)'],
      rootDir: '<rootDir>',
      testEnvironment: 'jsdom',
    moduleNameMapper: {
      '\\.(css|scss)$': 'identity-obj-proxy',
      '\\.(png|jpg|svg)$': '<rootDir>/test/__mocks__/fileMock.js'
    }
  },
    {
      displayName: 'ui',
      testMatch: ['<rootDir>/packages/ui/src/**/*.test.(ts|tsx|js|jsx)'],
      rootDir: '<rootDir>',
      testEnvironment: 'jsdom',
      transform: {
        "^.+\\.(js|jsx|ts|tsx)$": "babel-jest"
      },
      moduleFileExtensions: ["js", "jsx", "ts", "tsx", "json", "node"],
      moduleNameMapper: {
        '\\.(css|scss)$': 'identity-obj-proxy',
        '\\.(png|jpg|svg)$': '<rootDir>/test/__mocks__/fileMock.js'
      }
    }
  ],
  moduleFileExtensions: ["js", "jsx", "ts", "tsx", "json", "node"],
  transformIgnorePatterns: []
};