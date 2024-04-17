class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1

  def __init__(self):
    self.__root = None

  def insert_element(self, value):
    # O(log n) because the tree is height balanced which makes it so that
    # performance is logarithmic (half of the tree is eliminated with each
    # traversal) based on the number of nodes.
    if self.__root == None:
      self.__root = self.__BST_Node(value)
    else:
      var = self.__root
      self.__insert_recursive(value, var)
  def __insert_recursive(self, value, var):
    if var == None:
      return self.__BST_Node(value)
    if value == var.value:
      raise ValueError
    if value > var.value:
      var.right = self.__insert_recursive(value, var.right)
    elif value < var.value:
      var.left = self.__insert_recursive(value, var.left)
    if var.left is not None or var.right is not None:
      var.height = max(self.__node_height(var.right), self.__node_height(var.left)) + 1
    return self.__balance(var)

  def remove_element(self, value):
    # O(log n) because the method finds a value in the AVL tree
    # which is height balanced.
    self.__root = self.__remove_recursive(self.__root, value)

  def __remove_recursive(self, node, value):
    if node is None:
      raise ValueError
    if value < node.value:
      node.left = self.__remove_recursive(node.left, value)
    elif value > node.value:
      node.right = self.__remove_recursive(node.right, value)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      node.value = self.__min_value(node.right)
      node.right = self.__remove_recursive(node.right, node.value)
    node.height = max(self.__node_height(node.left), self.__node_height(node.right)) + 1
    return self.__balance(node)
  def __node_height(self, node):
    if node is None:
      return 0
    return node.height
  def __min_value(self, node):
    # O(h) because the method visits the minimum node on each level
    # one time.
    current = node
    while current.left is not None:
      current = current.left
    return current.value

  def in_order(self):
    # O(n) because every node is visited once.
    if self.__root is None:
        return '[ ]'
    return '[ ' + self.__in_order_recursive(self.__root).rstrip(', ') + ' ]'
  def __in_order_recursive(self, node):
    if node is None:
        return ''
    result = []
    if node.left:
        result.append(self.__in_order_recursive(node.left))
    result.append(str(node.value))
    if node.right:
        result.append(self.__in_order_recursive(node.right))
    return ', '.join(result)

  def pre_order(self):
    # O(n) because every node in the tree is visited once.
    if self.__root is None:
        return '[ ]'
    return '[ ' + self.__pre_order_recursive(self.__root) + ' ]'
  def __pre_order_recursive(self, node):
    if node is None:
        return ''
    result = [str(node.value)]
    if node.left:
        result.append(self.__pre_order_recursive(node.left))
    if node.right:
        result.append(self.__pre_order_recursive(node.right))
    return ', '.join(result)
  
  def post_order(self):
    # O(n) because every node in the tree is visited once.
    if self.__root is None:
        return '[ ]'
    return '[ ' + self.__post_order_recursive(self.__root).rstrip(', ') + ' ]'
  def __post_order_recursive(self, node):
    if node is None:
        return ''
    result = []
    if node.left:
        result.append(self.__post_order_recursive(node.left))
    if node.right:
        result.append(self.__post_order_recursive(node.right))
    result.append(str(node.value))
    return ', '.join(result)

  def to_list(self):
    # O(n) because every node is visited once.
    return self.__to_list_recursive(self.__root)
  def __to_list_recursive(self, node):
    if node == None:
      return []
    result = []
    result.extend(self.__to_list_recursive(node.left))
    result.append(node.value)
    result.extend(self.__to_list_recursive(node.right))
    return result

  def get_height(self):
    # O(1) because it is simply fetching an attribute.
    if self.__root == None:
       return 0
    return self.__root.height

  def __str__(self):
    return self.in_order()

  def __balance(self, var):
    # O(1) because the method is calculating the difference in height
    # between the two subtrees, which is a fixed attribute.
    balance = self.__get_balance(var)
    balance_left = self.__get_balance(var.left)
    balance_right = self.__get_balance(var.right)
    if balance < -1:
      if balance_left <= 0:
        return self.__rotate_right(var)
      else:
        var.left = self.__rotate_left(var.left)
        return self.__rotate_right(var)
    elif balance > 1:
      if balance_right >= 0:
        return self.__rotate_left(var)
      else:
        var.right = self.__rotate_right(var.right)
        return self.__rotate_left(var)
    return var
  
  def __get_balance(self, var):
    # O(1) because the method is calculating the difference in height
    # between the two subtrees, which is a fixed attribute.
    if var is None:
      return 0
    left_height = var.left.height if var.left else 0
    right_height = var.right.height if var.right else 0
    return right_height - left_height
  
  def __rotate_right(self, var):
    # O(1) because the same number of changes are made each time
    # the method is called.
    var1 = var.left
    if var1 is None:
      return var
    floater = var1.right
    var1.right = var
    var.left = floater
    self.__height_updater(var)
    self.__height_updater(var1)
    if var == self.__root:
      self.__root = var1
    return var1
  
  def __rotate_left(self, var):
    # O(1) because the same number of changes are made each time
    # the method is called.
    var1 = var.right
    if var1 is None:
      return var
    floater = var1.left
    var1.left = var
    var.right = floater
    self.__height_updater(var)
    self.__height_updater(var1)
    if var == self.__root:
      self.__root = var1
    return var1
  
  def __height_updater(self, node):
    # O(1) because the same calculation is done every
    # time the function is called.
    if node == None:
        return 0
    else:
        right_height = self.__height_updater(node.right)
        left_height = self.__height_updater(node.left)
        node.height = max(right_height, left_height) + 1
        return node.height

if __name__ == '__main__':
  pass
