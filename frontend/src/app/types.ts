export interface OrderDetailsProps {
  subtotal: number;
  taxes: number;
  discounts: number;
  paid: boolean;
}

export interface ErrorProps {
  error: Error;
  reset: () => void;
}

// Order Model
export interface Item {
  name: string;
  price_per_unit: number;
  total: number;
}

export interface ItemOrdered {
  name: string;
  quantity: number;
}

export interface Round {
  created: string;
  items: ItemOrdered[];
}

export interface Order {
  subtotal: number;
  taxes: number;
  discounts: number;
  paid: boolean;
  items: Item[];
  rounds: Round[];
}
