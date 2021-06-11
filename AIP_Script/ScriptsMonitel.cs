using Monitel.TNA.AdaptationModule.Attributes;
using Microsoft.Practices.ServiceLocation;
using Microsoft.Practices.Prism.Events;
using Monitel.TNA.Terminal.Infrastructure.Events;
using Monitel.UI.Infrastructure.Services;
using Monitel.Mal;
using System;
using System.Numerics;
using Monitel.TNA.Terminal.Infrastructure.Interfaces.AnalysisTasks;
using System.Collections.Generic;
using Monitel.TNA.Terminal.Infrastructure;
using Monitel.TNA.MDA.Infrastructure;
using Monitel.EMS.Infrastructure.Settings.Interfaces;
using Monitel.EMS.Infrastructure.Settings;

[ScriptUnit(Name = "Установившийся режим")]

public class TestModule
{
    [ScriptMethod(Name="Скрипт для расчета УР")]
    public void TestScript()
    {
        var moduleId = new ModuleId();
        try
        {
            moduleId.Id = "Расчет режима(TP_PF_BB2BB_VA)";
            CommonService.StartMassUpdate();
            CommonService.RestrictDataAccess(moduleId);
            var tp =ServiceLocator.Current.GetInstance<ITopologyProcessor>();
            var lf =ServiceLocator.Current.GetInstance<ILoadflow>();
            var bb2bb =ServiceLocator.Current.GetInstance<IBB2BB2>();
            var va =ServiceLocator.Current.GetInstance<IViolationAnalysis>();
            if (tp.StartProcessingCommand.CanExecute(null))
               tp.StartProcessingCommand.Execute(null);
            if (tp.NeedToMakeTopology)
            {
              if (tp.SyncUpdatePowerSystemCommand.CanExecute(null))
                 tp.SyncUpdatePowerSystemCommand.Execute(null);
              else if (tp.SyncStartProcessingCommand.CanExecute(null))
                 tp.SyncStartProcessingCommand.Execute(null);
              else
              {
                 tp.SyncRemoveCreatedObjectsCommand.Execute(null);
                 tp.SyncStartProcessingCommand.Execute(null);
              }
            }
            if (lf.StartLoadflow.CanExecute(false))
               lf.SyncStartLoadflow.Execute(null);

            var powerFlowSourceUid = Guid.Parse("10000dae-0000-0000-c000-0000006d746c");
            var allocatedSourceUid = Guid.Parse("10000D96-0000-0000-C000-0000006D746C");

            if (bb2bb.DecompositionCommand.CanExecute(powerFlowSourceUid ))
               bb2bb.DecompositionCommand.Execute(powerFlowSourceUid );

            if (bb2bb.CalculationCommand.CanExecute(powerFlowSourceUid ))
               bb2bb.CalculationCommand.Execute(powerFlowSourceUid);

            var vaSettingsModel = ServiceLocator.Current.GetInstance<ITNAViolationAnalysisSettings>();
            vaSettingsModel.DataSourceUids = new List<Guid> { powerFlowSourceUid, allocatedSourceUid };
            vaSettingsModel.SwitchCurrentCalcKind = SwitchCurrentCalculationKind.UseExternalFunction;

            if (va.cmdClearVAResults.CanExecute(false))
               va.cmdSyncClearVAResults.Execute(null);

            if (va.cmdStartVA.CanExecute(false))
               va.cmdSyncStartVA.Execute(null);
        }
    catch (System.Exception ex)
        {
            var eventAggregator = ServiceLocator.Current.GetInstance<IEventAggregator>();
            eventAggregator.GetEvent<ProtocolMessageEvent>().
            Publish(new ProtocolMessage()
            {
                Content = ex.Message,
                Source = "TestScript",
            });
        }
    finally
        {
             Monitel.TNA.MDA.Infrastructure.CommonService.StopMassUpdate();
             CommonService.CancelRestrictDataAccess(moduleId);
        }
    }
}