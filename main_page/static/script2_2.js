let myChart1; // 첫 번째 차트 인스턴스
let myChart2; // 두 번째 차트 인스턴스

/**
 * 서버에서 보내는 Json 형식에 따른 script 
 */
// 서버에서 오는 데이터 (예시)
const responseData = [
    { "지역": "서울", "경력여부": "신입", "비율": 40 },
    { "지역": "서울", "경력여부": "경력", "비율": 30 },
    { "지역": "서울", "경력여부": "경력무관", "비율": 30 },
    { "지역": "부산", "경력여부": "신입", "비율": 30 },
    { "지역": "부산", "경력여부": "경력", "비율": 40 },
    { "지역": "부산", "경력여부": "경력무관", "비율": 30 },
    { "지역": "대구", "경력여부": "신입", "비율": 50 },
    { "지역": "대구", "경력여부": "경력", "비율": 20 },
    { "지역": "대구", "경력여부": "경력무관", "비율": 30 },
    { "지역": "광주", "경력여부": "신입", "비율": 20 },
    { "지역": "광주", "경력여부": "경력", "비율": 50 },
    { "지역": "광주", "경력여부": "경력무관", "비율": 30 },
    { "지역": "대전", "경력여부": "신입", "비율": 60 },
    { "지역": "대전", "경력여부": "경력", "비율": 30 },
    { "지역": "대전", "경력여부": "경력무관", "비율": 10 }
];

// JSON 데이터 변환 함수
function transformData(data) {
    const labels = [...new Set(data.map(item => item.지역))]; // 지역 이름 추출
    const datasets = {
        "신입": [],
        "경력": [],
        "경력무관": []
    };

    //저장시 자동정렬 어케 없애 ㅠㅠ 
    // labels.forEach(label => {
    //     const entry = data.filter(item => item.지역 === label);
    //     datasets.신입.push(entry.find(item => item.경력여부 === "신입") ? .비율 || 0);
    //     datasets.경력.push(entry.find(item => item.경력여부 === "경력") ? 비율 || 0);
    //     datasets.경력무관.push(entry.find(item => item.경력여부 === "경력무관") ? .비율 || 0);
    // });

    return {
        labels: labels,
        datasets: [{
                label: "신입",
                data: datasets.신입,
                backgroundColor: "rgba(75, 192, 192, 0.2)",
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 1
            },
            {
                label: "경력",
                data: datasets.경력,
                backgroundColor: "rgba(255, 99, 132, 0.2)",
                borderColor: "rgba(255, 99, 132, 1)",
                borderWidth: 1
            },
            {
                label: "경력무관",
                data: datasets.경력무관,
                backgroundColor: "rgba(255, 206, 86, 0.2)",
                borderColor: "rgba(255, 206, 86, 1)",
                borderWidth: 1
            }
        ]
    };
}

// 차트 그리기
function drawChart() {
    const ctx = document.getElementById('myChart1').getContext('2d');
    const jsonData = transformData(responseData); // 변환된 데이터 사용

    // 기존 차트가 있다면 제거
    if (myChart1) {
        myChart1.destroy();
    }

    const config = {
        type: 'bar',
        data: jsonData,
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: '비율 (%)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: '지역'
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: '지역별 신입/경력/경력무관 비중'
                }
            }
        }
    };

    // 차트 인스턴스 생성
    myChart1 = new Chart(ctx, config);
}

function drawChart2() {
    const ctx = document.getElementById('myChart2').getContext('2d');
    const jsonData = transformData(responseData); // 변환된 데이터 사용

    // 기존 차트가 있다면 제거
    if (myChart2) {
        myChart2.destroy();
    }

    const config = {
        type: 'bar',
        data: jsonData,
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: '비율 (%)'
                    },
                    stacked: true // Y축 스택 사용
                },
                x: {
                    title: {
                        display: true,
                        text: '지역'
                    },
                    stacked: true // X축 스택 사용
                }
            },
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: '지역별 신입/경력/경력무관 비중'
                }
            }
        }
    };

    // 차트 인스턴스 생성
    myChart2 = new Chart(ctx, config);
}

function showChart(chartNumber) {
    // 모든 차트 내용 숨기기
    const charts = document.querySelectorAll('.chart-content');
    charts.forEach(chart => {
        chart.style.display = 'none';
    });
    // 선택한 차트 내용 표시
    const selectedChart = document.getElementById('chart-' + chartNumber);
    if (selectedChart) {
        selectedChart.style.display = 'block';
    }
    // 차트 그리기
    if (chartNumber === 2) { // 두 번째 버튼 클릭 시
        drawChart();
        drawChart2();
    }
}


// 차트를 그리는 함수
function drawChart3() {
    const ctx = document.getElementById('myChart2').getContext('2d');
    const myChart2 = new Chart(ctx, {
        type: 'bar', // 차트 타입
        data: programmingData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// HTML 문서가 완전히 로드된 후 차트를 그립니다.
document.addEventListener('DOMContentLoaded', (event) => {
    drawChart2();
});