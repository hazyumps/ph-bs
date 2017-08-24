var topologyData = {
    nodes: [
        {"id": 0,  "name": "12K-1"},
        {"id": 1,  "name": "12K-2"},
        {"id": 2,  "name": "Of-9k-03"},
        {"id": 3,  "name": "Of-9k-02"},
        {"id": 4,  "name": "Of-9k-01"}
    ],
    links: [
        {"source": 0, "target": 1},
        {"source": 1, "target": 2},
        {"source": 1, "target": 3},
        {"source": 4, "target": 1},
        {"source": 2, "target": 3},
        {"source": 2, "target": 0},
        {"source": 3, "target": 0},
        {"source": 3, "target": 0},
        {"source": 3, "target": 0},
        {"source": 0, "target": 4},
        {"source": 0, "target": 4},
        {"source": 0, "target": 3}
    ]
};