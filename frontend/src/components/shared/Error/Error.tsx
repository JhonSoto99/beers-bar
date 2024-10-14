type ErrorProps = {
  error: string;
};

export const Error = ({ error }: ErrorProps) => {
  return <h1>{error}</h1>;
};
