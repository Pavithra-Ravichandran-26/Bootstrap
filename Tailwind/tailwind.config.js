```javascript
/** @type {import('tailwindcss').Config} */

module.exports = {
    content: ["./index.html"],

    theme: {
        extend: {
            colors: {
                profileBlue: "#2563EB",
                profileLight: "#EFF6FF"
            },

            fontFamily: {
                profile: ["Poppins", "sans-serif"]
            },

            borderRadius: {
                profile: "25px"
            }
        }
    },

    plugins: []
}
```
