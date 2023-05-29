//
//  main.swift
//  11650_좌표 정렬하기
//
//  Created by 예강이다 on 2023/05/21.
//

import Foundation

let N = Int(readLine()!)!
var arr = [(Int, Int)]()

for _ in 0..<N {
    let input = readLine()!.split(separator: " ").map{ Int($0)! }
    arr.append((input[0], input[1]))
}

// 1 1 / 1 2
arr.sort(by: {
    $0.0 == $1.0 ? $0.1 < $1.1 : $0.0 < $1.0
})

for i in 0..<N {
    print("\(arr[i].0) \(arr[i].1)")
}
