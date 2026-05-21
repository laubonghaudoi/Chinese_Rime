import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";

export default defineConfig({
  site: "https://laubonghaudoi.github.io",
  base: "/Chinese_Rime",
  integrations: [mdx()],
  trailingSlash: "always",
  build: {
    format: "directory"
  }
});
