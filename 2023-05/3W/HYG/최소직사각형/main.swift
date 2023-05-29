//
//  main.swift
//  최소직사각형
//
//  Created by 예강이다 on 2023/05/20.
//

import Foundation

let sizes = [[60,50], [30,70], [60,30], [80,40]]

var w = 0
var h = 0

for size in sizes {
    let width = max(size[0], size[1])
    let height = min(size[0], size[1])
    
    w = max(width, w)
    h = max(height, h)
}

print(w*h)

// 풀이1.
//var maxNum = 0
//var minNum = 0
//
//for size in sizes {
//    maxNum = max(maxNum, size.max()!)
//    minNum = max(minNum, size.min()!)
//}
//return maxNum * minNum
