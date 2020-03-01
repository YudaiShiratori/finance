from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField("会社名", max_length=30, blank=False)

    def _str_(self):
        return str(self.name)

class Fstatement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fiscal_year = models.DateField("決算日")
    bs_current_assets = models.IntegerField("流動資産（百万円）", default=0)
    bs_fixed_assets = models.IntegerField("固定資産（百万円）", default=0)
    bs_deferred_assets = models.IntegerField("繰延資産（百万円）", default=0)
    bs_current_liabilities = models.IntegerField("流動負債（百万円）", default=0)
    bs_fixed_liabilities = models.IntegerField("固定負債（百万円）", default=0)
    bs_net_assets = models.IntegerField("純資産（百万円）", default=0)
    pl_gross_sales = models.IntegerField("総売上（百万円）", default=0)
    pl_gross_profit = models.IntegerField("売上総利益（百万円）", default=0)
    pl_operating_profit = models.IntegerField("営業利益（百万円）", default=0)
    pl_ordinary_income = models.IntegerField("経常利益（百万円）", default=0)
    pl_income_before_tax = models.IntegerField("税引前当期純利益（百万円）", default=0)
    pl_net_income = models.IntegerField("当期純利益（百万円）", default=0)
    cf_operating = models.IntegerField("営業ＣＦ（百万円）", default=0)
    cf_investment = models.IntegerField("投資ＣＦ（百万円）", default=0)
    cf_finance = models.IntegerField("財務ＣＦ（百万円）", default=0)

    def _str_(self):
        return str(self.company) + '決算日：【' + str(self.fiscal_year) + '】'

     # 総資産
    def bs_total_assets(self):
        f = self.bs_current_assets + self.bs_fixed_assets + self.bs_deferred_assets
        return f

    # 流動資産比率（流動資産／総資産）
    def current_assets_rate(self):
        f = self.bs_current_assets / self.bs_total_assets() * 100
        return f

    # 固定資産比率（固定資産／総資産）
    def fixed_assets_rate(self):
        f = self.bs_fixed_assets / self.bs_total_assets() * 100
        return f

    # 繰延資産比率（繰延資産／総資産）
    def deferred_assets_rate(self):
        f = self.bs_deferred_assets / self.bs_total_assets() * 100
        return f

    # 流動負債比率（流動負債／総資産）
    def current_liabilities_rate(self):
        f = self.bs_current_liabilities / self.bs_total_assets() * 100
        return f

    # 固定負債比率（固定負債／総資産）
    def fixed_liabilities_rate(self):
        f = self.bs_fixed_liabilities / self.bs_total_assets() * 100
        return f

    # 純資産比率（純資産／総資産）
    def net_assets_rate(self):
        f = self.bs_net_assets / self.bs_total_assets() * 100
        return f

    # 売上総利益比率（売上総利益／総売上）
    def gross_profit_rate(self):
        f = self.pl_gross_profit / self.pl_gross_sales * 100
        return f

    # 営業利益比率（営業利益／総売上）
    def operating_profit_rate(self):
        f = self.pl_operating_profit / self.pl_gross_sales * 100
        return f

    # 経常利益比率（経常利益／総売上）
    def ordinary_income_rate(self):
        f = self.pl_ordinary_income / self.pl_gross_sales * 100
        return f

    # 税引前当期純利益比率（税引前当期純利益／総売上）
    def income_before_tax_rate(self):
        f = self.pl_income_before_tax / self.pl_gross_sales * 100
        return f

    # 当期純利益比率（当期純利益／総売上）
    def net_income_rate(self):
        f = self.pl_net_income / self.pl_gross_sales * 100
        return f

    # キャッシュフロー
    def cf_total_amount(self):
        f = self.cf_operating + self.cf_investment + self.cf_finance
        return f
