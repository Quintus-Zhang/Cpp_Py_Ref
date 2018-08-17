#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <iomanip>
#include <fstream>

using namespace std;

void syntax_var_assign(){
    // variable assignment
    // In C++, the variable 'a' refers to a location in memory, and the value "hello" is inserted in that location
    string a = "Hello";
    cout << a << " is stored at " << &a << endl;
    // now the contents of the memory location referred to by 'a' are changed to "World"
    a = "World";
    cout << a << " is stored at " << &a << endl;
}

void syntax_print(){
    cout << "Hello, World!" << endl;
}

void syntax_for(){
    for (int i=0; i<5; i++)
        cout << i;
    cout << endl;
}

void syntax_for_continue(){
    for (int i=0; i<5; i++){
        if (i % 2 == 1)
            continue;
        cout << i;
    }
    cout << endl;
}

void syntax_for_break(){
    for (int i=0; i<5; i++){
        if (i >= 3)
            break;
        cout << i;
    }
    cout << endl;
}

void syntax_while(){
    int i = 0;
    while (i < 5){
        cout << i++;
    }
    cout << endl;
}

void syntax_while_continue(){
    int i = 0;
    while (i < 5){
        if (i % 2 == 1){
            i++;
            continue;
        }
        cout << i++;
    }
    cout << endl;
}

void syntax_while_break(){
    int i = 0;
    while (i < 5){
        if (i >= 3)
            break;
        cout << i;
        i++;
    }
    cout << endl;
}

void syntax_do_while(){
    int i = 0;
    do {
        cout << i++;
    } while(i < 5);
    cout << endl;
}

void syntax_do_while_continue(){
    int i = 0;
    do {
        if (i % 2 == 1){
            i++;
            continue;
        }
        cout << i++;
    } while(i < 5);
    cout << endl;
}

void syntax_do_while_break(){
    int i = 0;
    do {
        cout << i++;
        if (i >= 3)
            break;
    } while(i < 5);
    cout << endl;
}

void syntax_if_else(){
    int s = 1;
    if (s)
        cout << s << endl;
    else
        cout << !s << endl;
}

void syntax_logical_op(int s, int t){
    if (s && t)
        cout << "s = " << s << ", t = " << t << ", s && t = " << s && t;
    else if (s || t)
        cout << "s = " << s << ", t = " << t << ", s || t = " << s || t;
    else 
        cout << "s = " << s << ", t = " << t << ", !s = " << !s << ", !t = " << !t ;
    cout << endl;
}

void ds_array_1(){
    double arr[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};
    for (int i=0; i<5; i++)
        cout << arr[i] << ", ";
    cout << endl;  
    cout << "size of arr: " << sizeof(arr)/sizeof(arr[0]) << endl;
}

void ds_vector(){
    vector<int> vec;
    
    // push_back
    cout << "empty vector --> ";
    for(int i = 0; i < 5; i++)
       vec.push_back(i);
    for(int i = 0; i < vec.size(); i++)
       cout << vec[i];
    cout << endl;

    // pop_back
    cout << "             --> ";
    vec.pop_back();
    for(int i = 0; i < vec.size(); i++)
       cout << vec[i];
    cout << endl;

    // insert
    cout << "             --> ";
    vec.insert(vec.begin(), 9);
    for(int i = 0; i < vec.size(); i++)
       cout << vec[i];
    cout << endl;

    // erase
    cout << "             --> ";
    vec.erase(vec.begin());
    for(int i = 0; i < vec.size(); i++)
       cout << vec[i];
    cout << endl;
    
    // clear
    cout << "             --> ";
    vec.clear();
    for(int i = 0; i < vec.size(); i++)
       cout << vec[i];
    cout << endl;
}

void ds_map(){
    map<char, int> a_map = {
        {'a', 1},
        {'b', 3},
        {'c', 5},
        {'d', 7},
    };

    // Returns a reference to the mapped value of the element identified with key k
    cout << a_map.at('a') << endl;
    
    // Test if a certain key exist in the map
    cout << a_map.count('d') << '\t' << a_map.count('e') << endl;
    
    // Insert a new element if its key is unique.
    a_map.emplace('x', 9);
    cout << a_map['x'] << endl;

    // Search the map for an element with specified key, return an iterator if found, 
    // otherwie, returns and iterator to map::end
    map<char, int>::iterator it;
    it = a_map.find('b');
    cout << it->second << endl;

    // 
}

void str_concatenate(){
    string s1 = "Hello";
    string s2 = "World";
    string s3;

    s3 = s1 + s2;
    cout << "s3 = s1 + s2 = " << s3 << endl;
    cout << "s3.size() = " << s3.size() << endl;
}

void str_find_substr(){
    string s ("Hello World! \nHaHa \tNaNa");
    cout << s.find("or") << endl;
    cout << s.find("\n") << endl;
    cout << s.find("\t") << endl;
}

void str_substr(){
    string s ("Hello World!");
    cout << s.substr(0, 5) << endl;
}

void str_num_format(){
    float n = 3.1415926;
    cout << setprecision(4) << n << endl;
}

void iter_cpp(){
    string s = "Hello, World!";
    for (string::iterator it=s.begin(); it!=s.end(); ++it){
        cout << *it;
    }
    cout << endl;
}

int add_b(int a, int b){
    a = a + b;
    return a;
}

int add_c(int& a, int& c){
    a = a + c;
    return a;
}

void io_write_read_1dvec_txt(){
    
    // write vector to txt
    vector<int> a {1, 2, 3, 4, 5};
    ofstream file_out("1d.txt");
    for(int i = 0; i < a.size(); i++)
        file_out << a[i] << '\t';
    file_out.close();

    // read vector from txt
    int num;
    vector<int> b;
    ifstream file_in("1d.txt");
    while (file_in >> num)
        b.push_back(num);
    file_in.close();

    for(int i = 0; i < b.size(); i++)
       cout << b[i];
    cout << endl;
}

void io_write_read_2dvec_txt(){
    
    // write 2d vector to txt
    vector<string> a {"ab", "cd", "ef", "gh", "ij"};
    vector<vector<string> > a_2d(3, a);
    ofstream file_out("2d.txt");
    for (int i = 0; i<a_2d.size(); i++){
        for (int j = 0; j < a_2d[i].size(); j++)
            file_out << a_2d[i][j] << '\t';
        file_out << '\n';
    }
    file_out.close();

    // read data from txt and store as 2d vector
    vector<vector<string>> b_2d;
    string line;

    ifstream file_in("2d.txt");
    while (getline(file_in, line)){
        b_2d.push_back(vector<string>());
        size_t start_pos = 0U;
        do {
            size_t end_pos = line.find('\t', start_pos);
            b_2d.back().push_back( line.substr( start_pos, end_pos-start_pos) );
            start_pos = end_pos + (end_pos != string::npos);
        } while (start_pos != string::npos);
    }

    for (int i = 0; i<b_2d.size(); i++){
        for (int j = 0; j < b_2d[i].size(); j++)
            cout << b_2d[i][j] << '\t';
        cout << '\n';
    }
}

class Shape {
    protected:
        int width, height;  
    public:
        Shape( int a = 0, int b = 0) {
            cout << "Object is being created" << endl; 
            width = a;
            height = b;
        }
        virtual int area() {
            cout << "Shape area: width is " << width << ", height is " << height <<endl;
            return 0;
        }
        ~Shape(){
            cout << "Object is being deleted" << endl;
        };
};

class Rectangle: public Shape {
    public:
        Rectangle( int a = 0, int b = 0):Shape(a, b) { }
        
        int area () { 
            cout << "Rectangle class area: " << width * height <<endl;
            return (width * height); 
        }

        void give_me_rec(int x){
            cout << "give me " << x << " rectangle" << endl;
            cout << "Area: " << x << " * " << width * height << " = " << x * width * height << endl;
        }
        void give_me_rec(double x){
            cout << "give me " << x << " rectangle" << endl;
            cout << "Area: " << x << " * " << width * height << " = " << x * width * height << endl;
        }
};

class Triangle: public Shape {
    public:
        Triangle( int a = 0, int b = 0):Shape(a, b) { }
      
        int area () { 
            cout << "Triangle class area: " << 0.5 * width * height <<endl;
            return (width * height / 2); 
      }
};


/* TODO: 
    - bitwise not 
*/

int main()
{
    // syntax: variable assignment
    syntax_var_assign();

    // syntax: print
    syntax_print();

    // syntax: for-loop
    syntax_for();

    // syntax: for-loop & continue
    syntax_for_continue();

    // syntax: for-loop & break
    syntax_for_break();

    // syntax: while-loop
    syntax_while();

    // syntax: while-loop & continue
    syntax_while_continue();

    // syntax: while-loop & break
    syntax_while_break();

    // syntax: do while
    syntax_do_while();

    // syntax: do while & continue
    syntax_do_while_continue();

    // syntax: do while & break
    syntax_do_while_break();

    // syntax: if-else
    syntax_if_else();

    // syntax: logical operators
    syntax_logical_op(0, 0);

    // data structure: array
    ds_array_1();

    // data structure: vector
    ds_vector();

    // data structure: map
    ds_map();

    // string
    str_concatenate();
    str_find_substr();
    str_substr();
    str_num_format();

    // iterator
    iter_cpp();

    // function: pass-by-value
    int n = 10;
    int b = 5;
    cout << n << '\t';
    cout << add_b(n, b) << '\t';
    cout << n << endl;

    // function: pass-by-reference
    int c = 5;
    cout << n << '\t';
    cout << add_c(n, c) << '\t';
    cout << n << endl;

    // write and read text file
    io_write_read_1dvec_txt();
    io_write_read_2dvec_txt();

    // class: declaration & constructor & destructor
    Shape ape(0, 0);
    ape.area();

    // class: inheritance
    Rectangle rec(3, 4);
    rec.area();

    // class: function overloading
    Rectangle rec(1, 1);
    rec.give_me_rec(3);
    rec.give_me_rec(3.5);
    
    // class: polymorphism
    vector<Shape *> shapes;
    Rectangle rec(3, 4);
    Triangle tri(10, 5);
    shapes.push_back(&rec);
    shapes.push_back(&tri);
    for (int i=0; i<shapes.size(); i++)
        shapes[i]->area();

    return 0;
}