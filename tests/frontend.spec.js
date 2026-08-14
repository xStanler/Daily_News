import { test, expect } from '@playwright/test';

test.describe('Daily News frontend', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/frontend/index.html');
  });

  test('loads with correct title and structure', async ({ page }) => {
    await expect(page).toHaveTitle('Daily News');
    await expect(page.locator('nav')).toBeVisible();
    await expect(page.locator('main .articles')).toBeAttached();
    await expect(page.locator('footer')).toContainText('© 2026 Daily News.');
  });

  test('renders all category nav buttons with correct HTMX targets', async ({ page }) => {
    const categories = [
      { label: 'Sport', endpoint: '/articles/sport' },
      { label: 'Ekonomia', endpoint: '/articles/ekonomia' },
      { label: 'Polityka', endpoint: '/articles/polityka' },
      { label: 'Zdrowie', endpoint: '/articles/zdrowie' },
      { label: 'Technologia', endpoint: '/articles/technologia' },
    ];

    for (const { label, endpoint } of categories) {
      const btn = page.locator('.nav-btn', { hasText: label });
      await expect(btn).toHaveAttribute('hx-get', endpoint);
      await expect(btn).toHaveAttribute('hx-target', '.articles');
    }
  });

  test('logo links back to home feed', async ({ page }) => {
    const logo = page.locator('#logo');
    await expect(logo).toHaveAttribute('hx-get', '/home');
    await expect(logo).toHaveAttribute('hx-target', '.articles');
  });

  test('articles container auto-loads home feed on page load', async ({ page }) => {
    const articles = page.locator('main .articles');
    await expect(articles).toHaveAttribute('hx-get', '/home');
    await expect(articles).toHaveAttribute('hx-trigger', 'load');
  });

  test('clicking a nav button marks it selected and clears the previous selection', async ({ page }) => {
    const sport = page.locator('.nav-btn', { hasText: 'Sport' });
    const polityka = page.locator('.nav-btn', { hasText: 'Polityka' });

    await sport.click();
    await expect(sport).toHaveClass(/nav-btn-selected/);
    await expect(polityka).not.toHaveClass(/nav-btn-selected/);

    await polityka.click();
    await expect(polityka).toHaveClass(/nav-btn-selected/);
    await expect(sport).not.toHaveClass(/nav-btn-selected/);
  });

  test('only one nav button is selected at a time', async ({ page }) => {
    const buttons = page.locator('.nav-btn');
    const count = await buttons.count();
    for (let i = 0; i < count; i++) {
      await buttons.nth(i).click();
      await expect(page.locator('.nav-btn-selected')).toHaveCount(1);
    }
  });
});
