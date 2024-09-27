// src/tests/RoundList.test.tsx
import { render, screen } from "@testing-library/react";
import { RoundList } from "app/components/order/RoundList"; // Ajusta la ruta según tu estructura
import { Round } from "app/app/types"; // Asegúrate de que esta ruta sea correcta

describe("RoundList Component", () => {
  const rounds: Round[] = [
    {
      created: "2024-09-27T10:00:00Z", // Fecha de ejemplo
      items: [
        { name: "Item A", quantity: 2 }, // Ajusta la estructura según tu tipo ItemOrdered
        { name: "Item B", quantity: 1 },
      ],
    },
    {
      created: "2024-09-27T11:00:00Z",
      items: [{ name: "Item C", quantity: 1 }],
    },
  ];

  it("renders rounds correctly", () => {
    render(<RoundList rounds={rounds} />);

    // Verificar que los títulos de las rondas se muestren correctamente
    expect(screen.getByText(/Order Rounds/)).toBeInTheDocument();
    expect(screen.getByText(/Round 1 - Ordered at:/)).toBeInTheDocument();
    expect(screen.getByText(/Round 2 - Ordered at:/)).toBeInTheDocument();

    // Verificar que los nombres de los ítems de la primera ronda se muestren correctamente
    expect(screen.getByText("Item A")).toBeInTheDocument();
    expect(screen.getByText("Item B")).toBeInTheDocument();

    // Verificar que los nombres de los ítems de la segunda ronda se muestren correctamente
    expect(screen.getByText("Item C")).toBeInTheDocument();
  });

  it("renders nothing if rounds array is empty", () => {
    render(<RoundList rounds={[]} />);

    // Verificar que no haya títulos de rondas
    expect(screen.queryByText(/Order Rounds/)).not.toBeInTheDocument();
  });
});
