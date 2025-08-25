/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}",   // all HTML files inside templates/
    "./**/templates/**/*.{html,js}", // app-level templates
    "./static/**/*.{js,css}",        // any static JS/CSS
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
