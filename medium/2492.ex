defmodule Solution do

  @spec min_distance(dist :: [integer], spt_set :: [boolean], n :: integer) :: integer
  def min_distance(dist, spt_set, n) do
    min = -1
    min_index = -1

    for u <- 0..n do
      if (dist[u] < min && !spt_set[u]) || min == -1 do
        min = dist[u]
        min_index = u
      end
    end

    min_index
  end

  @spec min_score(n :: integer, roads :: [[integer]]) :: integer
  def min_score(n, roads) do
    adj_matrix = List.duplicate(List.duplicate(0, n), n)

    for c <- roads do
      List.replace_at(adj_matrix[c[0] - 1], c[1] - 1, c[2])
      List.replace_at(adj_matrix[c[1] - 1], c[0] - 1, c[2])
    end

    dist = for _ <- 0..n, do: -1
    List.replace_at(dist, 0, 0)
    spt_set = List.duplicate(false, n)

    for cout <- 0..n do
      x = min_distance(dist, spt_set, n)
      List.replace_at(spt_set, x, true)

      for y <- 0..n do
        if adj_matrix[x][y] > 0 && !spt_set[y] && dist[y] > dist[x] + adj_matrix[x][y] do
          List.replace_at(dist, y, dist[x] + adj_matrix[x][y])
        end
      end
    end

    dist[n]
  end

end
