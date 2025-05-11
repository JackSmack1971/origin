module.exports = {
  extends: ["eslint:recommended", "next/core-web-vitals", "turbo"],
  rules: {
    "@next/next/no-html-link-for-pages": "off",
    "react/jsx-key": "off",
  },
};