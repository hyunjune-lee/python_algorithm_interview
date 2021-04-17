#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int INF = 9999, SWITCHES_COUNT = 10, CLOCKS = 16;

const char linked[SWITCHES_COUNT][CLOCKS + 1] = {
"xxx.............",
"...x...x.x.x....",
"....x.....x...xx",
"x...xxxx........",
"......xxx.x.x...",
"x.x...........xx",
"...x..........xx",
"....xx.x......xx",
".xxxxx..........",
"...xxx...x...x.."
}

bool areAligned(const vector<int)& clocks)
{
    for (int clock = 0; clock < CLOCKS; ++clock)
        if (clocks[clock] != 12)
            return False;
    return True;
}

void push(vector<int> &clocks, int switch_idx)
{
    for (int clock = 0; clock < CLOCKS; ++clock)
        if (linked[swtch][clock] == 'x')
        {
            clocks[clock] += 3;
            if (clocks[clock] == 15)
                clocks[clock] = 3;
        }
}

int solve(vector<int> &clocks, int switch_idx)
{
    if (switch_idx == SWITCHES_COUNT)
        return areAligned(clocks) ? 0 : INF;
    int ret = INF;
    for (int cnt = 0; cnt < 4; ++cnt)
    {
        ret = min(ret, cnt + solve(clocks, switch_idx + 1))
            push(clocks, switch_idx)
    }
    return ret
}

int main()
{
    int c;
    cin >> c;
    string strInput;    // 띄어쓰기 기준으로 N개의 수를 입력받을 String
    vector<int> vecNum; // 입력받은 N개의 수를 저장할 Vector

    // 숫자 입력 받기
    cout << "숫자를 입력하세요 : ";
    getline(cin, strInput);

    // 문자열 출력
    cout << "문자열 : " << strInput << endl;

    string strNum = ""; // 각각의 숫자를 저장할 임시 String
    for (int i = 0; i < strInput.length(); i++)
    {
        if (strInput.at(i) == ' ')
        {
            // 현재까지 저장한 문자(숫자)들을 Vector에 추가 후 String 초기화
            vecNum.push_back(atoi(strNum.c_str()));
            strNum = "";
        }
        else
        {
            // 띄어쓰기가 나올 때까지 문자 더함
            strNum += strInput.at(i);
            continue;
        }
    }
    vecNum.push_back(atoi(strNum.c_str())); // 마지막 숫자도 벡터에 추가
}
