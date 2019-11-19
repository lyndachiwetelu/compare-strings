fn compare_strings(_first_string:String, _second_string:String) -> bool {
    let mut switch = false;
    for element in _first_string.chars() {
        if _second_string.contains(element){
            switch = true;
        }
    }
    return switch;
}


fn main() {
 let string_one = String::from("main");
 let string_two = String::from("themain");
 let result = compare_strings(string_one, string_two);
 if result == true {
     println!("True");
 } 
 else {
     println!("Not True");
 }
 }
