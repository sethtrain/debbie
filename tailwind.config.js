module.exports = {
  content: [
    "./apps/**/templates/**/*.html",
    "./apps/**/templatetags/*.py",
    "./templates/**/**/*.html",
    "./templates/*.html",
    "./debbie/urls.py"
  ],
  theme: {
    extend: {
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
