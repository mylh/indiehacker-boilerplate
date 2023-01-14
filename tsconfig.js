{
  "include": ["vite.config.js"],
  "compilerOptions": {
    "esModuleInterop": true,
    "baseUrl": ".",
    "jsx": "react-jsx",
    "paths": {
      "@/*": ["web/frontend/*"]
    },
    "types": ["vite/client"]
  }
}
