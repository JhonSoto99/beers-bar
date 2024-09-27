import { beersBarBackendUrls } from "./urls";

export const getOrderSummary = async () => {
  const response = await fetch(beersBarBackendUrls.order.get, {});

  if (!response.ok) {
    throw new Error("Failed to fetch order summary");
  }
  return await response.json();
};
