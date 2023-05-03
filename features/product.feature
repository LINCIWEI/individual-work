 Feature: Add and remove products from shopping cart
  As a customer
  I want to be able to add and remove products from my shopping cart
  So that I can manage my purchases easily

  Scenario: Add product to cart
    Given I am a logged-in user
    When I add a product to my shopping cart
    Then the product should be added to my cart

  Scenario: Remove product from cart
    Given I am a logged-in user
    And I have a product in my cart
    When I remove the product from my cart
    Then the product should be removed from my cart