
class LinkedNode {
    int key;
    int value;
    LinkedNode next;
    LinkedNode prev;

    public LinkedNode(int key, int value) {
        this.key = key;
        this.value = value;
    }
}
class LRUCache {
    private Map<Integer, LinkedNode> key2node;
    private int capacity;
    private LinkedNode head;
    private LinkedNode tail;


    public LRUCache(int capacity) {
        this.key2node = new HashMap<>();
        this.capacity =  capacity;
        this.head = new LinkedNode(-1, -1);
        this.tail = new LinkedNode(-1, -1);

        head.next = tail;
        tail.prev = head;

    }
    
    public int get(int key) {
        if (key2node.containsKey(key)){
            LinkedNode node = key2node.get(key);
            remove(key, node);
            insert(key, node);
            return node.value;
        } else{
            return -1;
        }
    }
    
    public void put(int key, int value) {
        
        if (key2node.containsKey(key)){
            LinkedNode target = key2node.get(key);
            remove(target.key, target);
            LinkedNode newNode = new LinkedNode(key, value);
            insert(key, newNode);

        }else{
            if(key2node.size() == capacity){
                LinkedNode target = tail.prev;
                remove(target.key, target);
            }
            LinkedNode newNode = new LinkedNode(key, value);
            insert(key, newNode);
        }
    }

    private void remove(int key, LinkedNode node){
        LinkedNode prev = node.prev;
        LinkedNode next = node.next;

        prev.next = next;
        next.prev = prev;

        node.next = null;
        node.prev = null;

        key2node.remove(key);
        
    }

    private void insert(int key, LinkedNode node){
        LinkedNode next = head.next;

        head.next = node;
        next.prev = node;

        node.next = next;
        node.prev = head;

        key2node.put(key, node);
    }



}
