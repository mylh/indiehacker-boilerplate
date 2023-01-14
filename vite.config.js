import {resolve} from 'path';
import react from '@vitejs/plugin-react';
import tsconfigPaths from 'vite-tsconfig-paths';
import eslint from 'vite-plugin-eslint';


module['exports'] = {
    plugins: [react({}), tsconfigPaths(), eslint()],
    root: resolve('./web/frontend'),
    base: '/static/',
    server: {
        host: '0.0.0.0',
        port: 3000,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false,
        },
    },
    resolve: {
        extensions: ['.js', '.json', '.jsx', '.ts', '.tsx'],
        alias: {
            '~bootstrap': '/app/node_modules/bootstrap',
            '~bootstrap-icons': '/app/node_modules/bootstrap-icons',
        }
    },
    build: {
        outDir: resolve('./web/frontend/dist'),
        assetsDir: '',
        manifest: true,
        emptyOutDir: true,
        target: 'es2015',
        rollupOptions: {
            input: {
                main: resolve('./web/frontend/main.ts'),
            },
            output: {
                entryFileNames: '[name].js',
                chunkFileNames: '[name].js',
                assetFileNames: '[name].[ext]'
            }
        }
    },
};
