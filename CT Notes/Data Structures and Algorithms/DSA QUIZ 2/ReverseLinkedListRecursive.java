class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
    }
}

public class ReverseLinkedListRecursive {
    public ListNode reverseList(ListNode head) {
        // Base case: If the list is empty or has only one node, return the head
        if (head == null || head.next == null) {
            return head;
        }

        // Recursively reverse the rest of the list
        ListNode reversedList = reverseList(head.next);

        // Move the current node to the end
        head.next.next = head;
        head.next = null;

        // Return the new head of the reversed list
        return reversedList;
    }

    public static void main(String[] args) {
        // Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        // Reverse the linked list
        ReverseLinkedListRecursive solution = new ReverseLinkedListRecursive();
        ListNode reversedHead = solution.reverseList(head);

        // Print the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
        ListNode current = reversedHead;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
    }
}

