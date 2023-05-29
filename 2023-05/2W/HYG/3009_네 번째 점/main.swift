//
//  main.swift
//  3009_네 번째 점
//
//  Created by 예강이다 on 2023/05/16.
//

import Foundation

var arrX = Array(repeating: 0, count: 1001)
var arrY = Array(repeating: 0, count: 1001)

for _ in 0...2 {
    let input = readLine()!.split(separator: " ").map{ Int($0)! }
    let A = input[0]
    let B = input[1]
    
    arrX[A] += 1
    arrY[B] += 1
}

for i in 1...1000 {
    if arrX[i] == 1 {
        arrX[0] = i
    }
    if arrY[i] == 1 {
        arrY[0] = i
    }
}

print("\(arrX[0]) \(arrY[0])")
