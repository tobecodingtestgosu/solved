//
//  main.swift
//  10773_제로
//
//  Created by 예강이다 on 2023/05/12.
//

import Foundation

let K = Int(readLine()!)!

var arr = [Int]()

for _ in 1...K {
    let n = Int(readLine()!)!
    
    if n != 0 {
        arr.append(n)
    } else {
        if !arr.isEmpty {
            arr.removeLast()
        }
    }
}
print(arr.reduce(0, +))
