module.exports = {
  ignores: ['node_modules/**', 'dist/**', 'build/**'],
  languageOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  linterOptions: {
    reportUnusedDisableDirectives: true
  },
  rules: {
    'no-unused-vars': 'warn',
    'no-console': 'off'
  }
};
