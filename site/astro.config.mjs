import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://laubonghaudoi.github.io",
  base: "/Chinese_Rime",
  trailingSlash: "always",
  build: {
    format: "directory"
  }
});
