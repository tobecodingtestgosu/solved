//
//  main.swift
//  1181_단어 정렬
//
//  Created by 예강이다 on 2023/04/04.
//

import Foundation

let N = Int(readLine()!)!
var arr = [String]()
var setArr = Set<String>()

for _ in 0..<N {
    let input = readLine()!
    setArr.insert(input)
}
//Array(Set(arr).sorted(by: {$0<$1}).sorted(by: {$0.count<$1.count}))
arr = Array(setArr).sorted(by: {$0 < $1}).sorted(by: {$0.count < $1.count})

for i in arr {
    print(i)
}
