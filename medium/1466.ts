const minReorder = (n: number, connections: number[][]): number => {
    const edges: number[][] = Array(n);
    for (let i = 0; i < n ; i++) edges[i] = Array(n).fill(0);
    for (const edge of connections) edges[edge[0]][edge[1]] = 1;

    let res = 0;
    const queue = [0];
    const visited = new Set<number>();
    while (queue.length > 0) {
        const c = queue.pop() || 0;

        for (let i = 0; i < n; i++) {
            if (i === c) continue;
            if (edges[c][i] === 1 && !visited.has(i)) {
                res += 1;
                edges[c][i] = 0;
                edges[i][c] = 1;
            }
        }

        for (let i = 0; i < n; i++) {
            if (edges[i][c] === 1) 
                queue.push(i);
        }

        visited.add(c);
    }

    return res;
};

console.log(minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]));
