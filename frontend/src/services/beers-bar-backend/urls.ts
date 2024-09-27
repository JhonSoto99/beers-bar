import { env } from "app/config/env";

export const beersBarBackendUrls = {
  order: {
    get: `${env.API_URL}/api/v1/order`,
  },
};
