const data = {
    type:'FeatureCollection',
    properties: {
        foo: 'qwe',
    },
    features: [
        {
            type:'Feature',
            name:'Сумска',
            geometry: {
                type:'MultiPolygon',
                coordinates: [
                    [
                        [35.3984695,50.9090683],
                        [35.398120000000006,50.9091],
                        [35.39833810000001,50.9092459],
                        [35.3984695,50.9090683],
                    ],
                ],
            },
        },
    ],
};
const layer = {
    id: 'my-polygons-layer',
    filter: [
        'match',
        ['sourceAttr', 'bar'],
        ['asd'],
        true,
        false,
    ],
    type: 'MultiPolygon',
    style: {
        color: '#0000ff',
    },
};
const source = new mapgl.GeoJsonSource(map, {
    data,
});
export {source, layer};