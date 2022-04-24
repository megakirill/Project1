const cordinates = [[35.3984695,50.9090683],[35.398120000000006,50.9091],[35.39833810000001,50.9092459],[35.3984695,50.9090683]]
const polygon = new mapgl.Polygon(map, {
    coordinates: [cordinates],
    color: '#990000',
    strokeWidth: 3,
    strokeColor: '#bb0000',
});

polygon.on('click', () => {
    alert('Polygon click');
});
