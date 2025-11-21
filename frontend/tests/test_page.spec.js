import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');
  await page.getByRole('button', { name: 'Test Health Check' }).click();
  await page.getByText('Status:').click();
  await page.getByRole('heading', { name: 'DevSecOps Python+FastAPI' }).click();
  await page.getByText('Status: Application runs!').click();
  await page.getByRole('button', { name: 'Test Health Check' }).click();
  await page.getByText('{ "status": "ok", "service').click();
  await page.getByRole('button', { name: 'Test Health Check' }).click();
  await page.getByText('Status: Application runs!').click();
  await page.getByRole('button', { name: 'Test Health Check' }).click();
  await page.getByRole('button', { name: 'Load Users' }).click();
  await page.getByRole('heading', { name: 'John Doe' }).click();
  await page.getByText('john.doe@example.com').click();
  await page.getByText('30 years').click();
  await page.getByText('admin').click();
  await page.getByRole('heading', { name: 'Jane Smith' }).click();
  await page.locator('html').click();
  await page.getByRole('heading', { name: 'Bob Johnson' }).click();
  await page.getByText('Alice Brown alice.brown@').click();
});


test('Health check and load users', async ({ page }) => {
  // Navigate to home page
  await page.goto('http://127.0.0.1:8000');

  // Click on button "Test Health Check"
  await page.getByRole('button', { name: /Test Health Check/i }).click();

  // Verify if status test apeare 
  await expect(page.getByText('Status: Application runs!')).toBeVisible();

  // Click on button "Load Users"
await page.getByRole('button', { name: /Load Users/i }).click();

// Wait for at least 4 user headings to appear
const userRows = page.locator('h3');

// Retry loop until count >= 4 or timeout
await page.waitForFunction(() => {
  return document.querySelectorAll('h3').length >= 4;
}, null, { timeout: 5000 });

  // Verify some users 
  await expect(page.getByText(/John Doe/i)).toBeVisible();
  await expect(page.getByText(/Jane Smith/i)).toBeVisible();
  await expect(page.getByText(/Bob Johnson/i)).toBeVisible();
  await expect(page.getByText(/Alice Brown/i)).toBeVisible();
});