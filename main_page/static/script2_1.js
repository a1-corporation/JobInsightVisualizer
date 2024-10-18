let myChart1; // 차트 인스턴스를 저장할 변수
let myChart2; // 차트 인스턴스를 저장할 변수 2

// JSON 데이터
const jsonData = {
    "labels": ["서울", "부산", "대구", "광주", "대전"],
    "datasets": [{
        "label": "신입",
        "data": [40, 30, 50, 20, 60],
        "backgroundColor": "rgba(75, 192, 192, 0.6)", // 더 부드러운 색상
        "borderColor": "rgba(75, 192, 192, 1)",
        "borderWidth": 1
    }, {
        "label": "경력",
        "data": [30, 40, 20, 50, 30],
        "backgroundColor": "rgba(255, 99, 132, 0.6)",
        "borderColor": "rgba(255, 99, 132, 1)",
        "borderWidth": 1
    }, {
        "label": "경력무관",
        "data": [30, 30, 30, 30, 10],
        "backgroundColor": "rgba(255, 206, 86, 0.6)",
        "borderColor": "rgba(255, 206, 86, 1)",
        "borderWidth": 1
    }]
};

// 2번 차트 그려주기 
function drawChart() {
    const ctx = document.getElementById('myChart1').getContext('2d');

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

    myChart1 = new Chart(ctx, config);
}

//2-2 차트 
function drawChart2() {
    const ctx = document.getElementById('myChart2').getContext('2d');

    // 기존 차트가 있다면 제거
    if (myChart2) {
        myChart2.destroy();
    }

    const config = {
        type: 'bar', // 3D 차트 타입
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
                    stacked: true
                },
                x: {
                    title: {
                        display: true,
                        text: '지역'
                    },
                    stacked: true
                }
            },
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: '지역별 신입/경력/경력무관 비중 (3D)'
                }
            }
        }
    };

    myChart2 = new Chart(ctx, config);
}