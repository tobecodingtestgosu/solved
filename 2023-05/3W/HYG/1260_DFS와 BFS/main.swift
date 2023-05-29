//
//  main.swift
//  1260_DFS와 BFS
//
//  Created by 예강이다 on 2023/05/20.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
let N = input[0]    // 정점의 개수
let M = input[1]    // 간선의 개수
let V = input[2]    // 탐색을 시작할 정점의 번호

// idx 번호에 이어지는 정점 번호를 넣는 빈 2차원 배열 선언
// ex) 1-2,3일 때 [null][2,3]
var graph : [[Int]] = Array(repeating: [], count: N+1)
// 그 idx를 방문 했는지 확인하는 1차원 배열 false 초기화
var check = Array(repeating: false, count: N+1)
var result = ""

// 간선의 개수만큼 반복
for _ in 0..<M {
    let relation = readLine()!.split(separator: " ").map{ Int($0)! }
    let a = relation[0]
    let b = relation[1]
    
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
}

func dfs(_ now: Int) {
    check[now] = true
    result += "\(now) "
    
    for i in graph[now] {
        if !check[i] {
            dfs(i)
        }
    }
}

func bfs(_ now: Int) {
    var needVisited = [now]
    var visited = Set<Int>()
    
    while !needVisited.isEmpty {
        let node = needVisited.removeFirst()
        
        if !visited.contains(node) {
            visited.insert(node)
            result += "\(node) "
            needVisited.append(contentsOf: graph[node])
        }
    }
}

dfs(V)
print(result)
result = ""
bfs(V)
print(result)
