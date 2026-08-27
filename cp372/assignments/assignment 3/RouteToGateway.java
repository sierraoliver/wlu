import java.util.*;
import java.io.*;

/**
 * CP372 Assignment 3: Policy-Based Link State Routing
 * Sierra Oliver, 169067437
 * Valid path structure: source --(no gateways)--> SA --(no gateways)--> gateway
 *
 * Usage:
 *   java RouteToGateway             <- reads from stdin
 *   java RouteToGateway input.txt   <- reads from file
 */

public class RouteToGateway {

    static final long INF = Long.MAX_VALUE / 2;

    public static void main(String[] args) throws IOException {
        Scanner sc;
        
        //either read from file if on input line, or take console input
        if (args.length > 0) {
            sc = new Scanner(new File(args[0]));
        } 
        else {
            sc = new Scanner(System.in);
        }

        int n = sc.nextInt();

        long[][] weight = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                long val = sc.nextLong();
                weight[i][j] = (val == -1) ? INF : val;
            }
        }

        sc.nextLine();
        String[] gParts = sc.nextLine().trim().split("\\s+");

        Set<Integer> gatewaySet = new HashSet<>();
        List<Integer> gateways = new ArrayList<>();

        for (String g : gParts) {
            int gw = Integer.parseInt(g) - 1;
            gatewaySet.add(gw);
            gateways.add(gw);
        }
        Collections.sort(gateways);

        int sa = sc.nextInt() - 1;
        sc.close();

        //distances
        long[] distFromSA = forwardDijkstra(n, weight, sa);
        long[] distToSA = reverseDijkstraBlockGateways(n, weight, sa, gatewaySet);

        Map<Integer, long[]> distToGW = new HashMap<>();
        for (int gw : gateways) {
            distToGW.put(gw, reverseDijkstraNoBlock(n, weight, gw));
        }

        //non-gateway routers
        List<Integer> nonGateways = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!gatewaySet.contains(i)) {
                nonGateways.add(i);
            }
        }

        System.out.println(); // separate input line or console input from output
        for (int src : nonGateways) {
            System.out.println("Forwarding Table for " + (src + 1));
            System.out.println("To\tCost\tNext Hop");

            long costToSA = distToSA[src];

            for (int gw : gateways) {
                long costSAToGW = distFromSA[gw];

                if (costToSA == INF || costSAToGW == INF) {
                    System.out.println((gw + 1) + "\t-1\t-1");
                    continue;
                }

                long totalCost = costToSA + costSAToGW;
                List<Integer> nextHops = new ArrayList<>();

                if (src == sa) {
                    long[] rGW = distToGW.get(gw);

                    for (int nh = 0; nh < n; nh++) {
                        if (nh == src) continue;

                        if (weight[src][nh] < INF &&
                            rGW[nh] != INF &&
                            weight[src][nh] + rGW[nh] == costSAToGW &&
                            (nh == gw || !gatewaySet.contains(nh))) {

                            nextHops.add(nh);
                        }
                    }
                } 
                else {
                    for (int nh = 0; nh < n; nh++) {
                        if (nh == src) continue;
                        if (gatewaySet.contains(nh) && nh != sa) continue;

                        if (weight[src][nh] < INF &&
                            distToSA[nh] != INF &&
                            weight[src][nh] + distToSA[nh] == costToSA) {

                            nextHops.add(nh);
                        }
                    }
                }

                Collections.sort(nextHops);

                if (nextHops.isEmpty()) {
                    System.out.println((gw + 1) + "\t-1\t-1");
                } 
                else {
                    StringBuilder sb = new StringBuilder();
                    for (int i = 0; i < nextHops.size(); i++) {
                        if (i > 0) sb.append(",");
                        sb.append(nextHops.get(i) + 1);
                    }
                    System.out.println((gw + 1) + "\t" + totalCost + "\t" + sb);
                }
            }
            System.out.println();
        }
    }

    static long[] forwardDijkstra(int n, long[][] weight, int source) {
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[source] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0, source});
        boolean[] visited = new boolean[n];

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            int u = (int) curr[1];

            if (visited[u]) continue;
            visited[u] = true;

            for (int v = 0; v < n; v++) {
                if (weight[u][v] < INF) {
                    long nd = dist[u] + weight[u][v];
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.offer(new long[]{nd, v});
                    }
                }
            }
        }
        return dist;
    }

    static long[] reverseDijkstraBlockGateways(int n, long[][] weight, int dest, Set<Integer> gatewaySet) {
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[dest] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0, dest});
        boolean[] visited = new boolean[n];

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            int u = (int) curr[1];

            if (visited[u]) continue;
            visited[u] = true;

            if (gatewaySet.contains(u) && u != dest) continue;

            for (int v = 0; v < n; v++) {
                if (weight[v][u] < INF && !visited[v]) {
                    long nd = dist[u] + weight[v][u];
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.offer(new long[]{nd, v});
                    }
                }
            }
        }
        return dist;
    }

    static long[] reverseDijkstraNoBlock(int n, long[][] weight, int dest) {
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[dest] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0, dest});
        boolean[] visited = new boolean[n];

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            int u = (int) curr[1];

            if (visited[u]) continue;
            visited[u] = true;

            for (int v = 0; v < n; v++) {
                if (weight[v][u] < INF && !visited[v]) {
                    long nd = dist[u] + weight[v][u];
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.offer(new long[]{nd, v});
                    }
                }
            }
        }
        return dist;
    }
}
