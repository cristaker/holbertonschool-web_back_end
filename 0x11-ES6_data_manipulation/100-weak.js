export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  const endpointCallCount = weakMap.get(endpoint);
  if (endpointCallCount + 1 === 5) throw Error('Endpoint load is high');
  if (endpointCallCount) {
    weakMap.set(endpoint, endpointCallCount + 1);
  } else {
    weakMap.set(endpoint, 1);
  }
}