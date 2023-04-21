defmodule Solution do
  # we'll come back to this
  @spec make_connected(n :: integer, connections :: [[integer]]) :: integer
  def make_connected(n, connections) do
    edges = %{}

    for c <- connections do
      Map.put(edges, edges[0], edges[1])
      Map.put(edges, edges[1], edges[0])
    end

    recurse = fn c :: int ->  end
  end

  end
end
